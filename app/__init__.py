from flask import Flask ,redirect ,url_for
from .config import Config
from .extensions import db, login_manager
from .blueprints.auth import auth
from .blueprints.ventas import ventas
from .models import User  # Importa el modelo User

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
    app.register_blueprint(ventas, url_prefix='/ventas')

    # Ruta inicial
    @app.route('/')
    def home():
        return redirect(url_for('auth.login'))  # Redirige a la página de login

    return app

# Callback para cargar un usuario
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Busca el usuario por su ID en la base de datos
