from flask import Blueprint

auth = Blueprint('auth', __name__, template_folder='templates')

# Importar rutas después de definir el blueprint
from . import routes
