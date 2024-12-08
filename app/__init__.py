from flask import Flask
from .config import Config
from .extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)

    # Rutas iniciales
    @app.route('/')
    def home():
        return "Bienvenido a Farmacia Web"

    return app
