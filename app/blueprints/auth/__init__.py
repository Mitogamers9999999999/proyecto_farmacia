from flask import Blueprint

auth = Blueprint('auth', __name__, template_folder='templates')

from . import routes  # Importa las rutas del blueprint
