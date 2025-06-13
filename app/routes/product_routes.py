from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.models import Product
from app import db

product_bp = Blueprint("product", __name__)

@product_bp.route("/products", methods=["GET"])
@jwt_required()
def get_products():
    products = Product.query.all()
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "description": p.description,
        "price": p.price
    } for p in products])

@product_bp.route("/products", methods=["POST"])
@jwt_required()
def create_product():
    data = request.get_json()
    new_product = Product(
        name=data["name"],
        description=data.get("description", ""),
        price=data["price"]
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product created"}), 201

@product_bp.route("/products/<int:product_id>", methods=["PUT"])
@jwt_required()
def update_product(product_id):
    data = request.get_json()
    product = Product.query.get_or_404(product_id)
    product.name = data["name"]
    product.description = data.get("description", "")
    product.price = data["price"]
    db.session.commit()
    return jsonify({"message": "Product updated"}), 200

@product_bp.route("/products/<int:product_id>", methods=["DELETE"])
@jwt_required()
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted"}), 200
