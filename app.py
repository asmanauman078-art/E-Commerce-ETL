
from flask import Flask, jsonify, render_template, send_from_directory
import requests
import pandas as pd 
import os
from pydantic import BaseModel, ValidationError

app = Flask(__name__)
class ProductModel(BaseModel):
    id: int
    title: str
    price: float
    category: str
    rating: float
    stock: int
    brand: str
    thumbnail: str

# DummyJSON API URL
API_URL = "https://dummyjson.com/products"


# EXTRACT: Fetch products from API
def extract_products():
    response = requests.get(API_URL, timeout=15)
    response.raise_for_status()

    data = response.json()
    products = data["products"]

    return products


# Home route
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/reports/<filename>")
def show_report(filename):
    return send_from_directory("reports", filename)
@app.route("/download-csv")
def download_csv():
    return send_from_directory(
        "outputs",
        "products.csv",
        as_attachment=True
    )


def transform_products(products):
    clean_products = []

    for product in products:
        clean_product = {
            "id": product.get("id"),
            "title": product.get("title", "Unknown"),
            "price": product.get("price", 0),
            "category": product.get("category", "Unknown"),
            "rating": product.get("rating", 0),
            "stock": product.get("stock", 0),
            "brand": product.get("brand", "Unknown"),
            "thumbnail": product.get("thumbnail", "")
        }

        try:
            validated_product = ProductModel(**clean_product)
            clean_products.append(validated_product.model_dump())

        except ValidationError as error:
            print("Invalid product:", error)

    return clean_products

    # LOAD: Save cleaned products into CSV
def load_products(clean_products):
    output_folder = "outputs"
    os.makedirs(output_folder, exist_ok=True)

    file_path = os.path.join(output_folder, "products.csv")

    df = pd.DataFrame(clean_products)
    df.to_csv(file_path, index=False)

    return file_path

# Products API route
@app.route("/api/products")
def get_products():
    try:
        products = extract_products()
        clean_products = transform_products(products)
        csv_file = load_products(clean_products)

        return jsonify({
            "success": True,
            "total_products": len(clean_products),
            "csv_file": csv_file,
            "products": clean_products
        })

    except requests.RequestException as error:
        return jsonify({
            "success": False,
            "error": str(error)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)


