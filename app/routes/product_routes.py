from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models import db, Product

product_bp = Blueprint("product", __name__)

@product_bp.route("/api/products", methods=["GET"])
@jwt_required()
def get_products():
    products = Product.query.all()
    return jsonify([
        {"id": p.id, "name": p.name, "description": p.description, "price": p.price}
        for p in products
    ])

@product_bp.route("/api/products", methods=["POST"])
@jwt_required()
def create_product():
    data = request.get_json()
    product = Product(
        name=data["name"],
        description=data["description"],
        price=data["price"]
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "Product created", "id": product.id}), 201

@product_bp.route("/api/products/<int:id>", methods=["PUT"])
@jwt_required()
def update_product(id):
    data = request.get_json()
    product = Product.query.get_or_404(id)
    product.name = data["name"]
    product.description = data["description"]
    product.price = data["price"]
    db.session.commit()
    return jsonify({"message": "Product updated"})

@product_bp.route("/api/products/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted"})