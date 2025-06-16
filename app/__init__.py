from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# Define these before using
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://catalog_user:catalog_pass@127.0.0.1:5432/catalog"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "your_secret_key_here"

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    CORS(app)

    from app.routes.auth_routes import auth_bp
    from app.routes.product_routes import product_bp
    from app.routes.ui_routes import ui_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(ui_bp)

    return app