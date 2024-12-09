from flask import Flask
from .config import Config
from .extensions import db, login_manager
from .blueprints.auth import auth
from .models import User

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)

    # Configurar la vista de inicio de sesión predeterminada
    login_manager.login_view = 'auth.login'

    # Registrar blueprints
    app.register_blueprint(auth, url_prefix='/auth')

    # Rutas iniciales
    @app.route('/')
    def home():
        return "Bienvenido a Farmacia Web"

    return app

# Callback para cargar el usuario
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
