from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    db.create_all()  # Crear tablas si no existen

    # Crear un usuario de prueba
    user = User(username='jose')
    user.set_password('huaycho')
    db.session.add(user)
    db.session.commit()

    print("Usuario creado: jose / huaycho")
