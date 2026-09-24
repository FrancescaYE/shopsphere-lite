from flask import Flask, render_template, request, redirect, url_for, abort
import os
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = Path(
    os.getenv("DATABASE_PATH", BASE_DIR / "instance" / "shopsphere.db")
)

app = Flask(__name__)


def get_db():
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    return connection


def init_db():
    with get_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL,
                description TEXT NOT NULL
            )
        """)

        count = db.execute(
            "SELECT COUNT(*) FROM products"
        ).fetchone()[0]

        if count == 0:
            products = [
                (
                    "Classic T-Shirt",
                    "Clothing",
                    15.00,
                    "Simple cotton t-shirt for everyday use."
                ),
                (
                    "Urban Sneakers",
                    "Shoes",
                    45.00,
                    "Comfortable sneakers for everyday city life."
                ),
                (
                    "Leather Bag",
                    "Accessories",
                    60.00,
                    "Compact bag for work and daily travel."
                ),
                (
                    "Smart Watch",
                    "Electronics",
                    80.00,
                    "Basic smart watch with activity tracking."
                ),
                (
                    "Wireless Headphones",
                    "Electronics",
                    35.00,
                    "Wireless headphones for music and calls."
                ),
                (
                    "Summer Dress",
                    "Clothing",
                    40.00,
                    "Light and comfortable dress for warm weather."
                ),
            ]

            db.executemany(
                """
                INSERT INTO products
                (name, category, price, description)
                VALUES (?, ?, ?, ?)
                """,
                products,
            )


@app.route("/")
def index():
    search = request.args.get("q", "").strip()

    with get_db() as db:
        if search:
            products = db.execute(
                """
                SELECT * FROM products
                WHERE name LIKE ? OR category LIKE ?
                ORDER BY id DESC
                """,
                (f"%{search}%", f"%{search}%"),
            ).fetchall()
        else:
            products = db.execute(
                "SELECT * FROM products ORDER BY id DESC"
            ).fetchall()

    return render_template(
        "index.html",
        products=products,
        search=search
    )


@app.route("/product/<int:product_id>")
def product(product_id):
    with get_db() as db:
        item = db.execute(
            "SELECT * FROM products WHERE id = ?",
            (product_id,)
        ).fetchone()

    if item is None:
        abort(404)

    return render_template(
        "product.html",
        product=item
    )


@app.route("/admin/products/new", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        category = request.form.get("category", "").strip()
        description = request.form.get("description", "").strip()

        try:
            price = float(request.form.get("price", "0"))
        except ValueError:
            price = 0

        if not name or not category or not description or price <= 0:
            return render_template(
                "admin_new.html",
                error="Please provide valid values for every field."
            )

        with get_db() as db:
            db.execute(
                """
                INSERT INTO products
                (name, category, price, description)
                VALUES (?, ?, ?, ?)
                """,
                (name, category, price, description),
            )

        return redirect(url_for("index"))

    return render_template(
        "admin_new.html",
        error=None
    )


@app.route("/health")
def health():
    return {"status": "ok"}


init_db()


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )
