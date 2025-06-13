from flask import Blueprint, render_template

ui_bp = Blueprint("ui", __name__)

@ui_bp.route("/")
def index():
    return render_template("index.html")

@ui_bp.route("/products")
def products_ui():
    return render_template("products.html")
