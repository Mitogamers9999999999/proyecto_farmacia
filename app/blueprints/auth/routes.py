from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from .forms import LoginForm
from app.models import User
from . import auth  # Importa el blueprint 'auth'

# Ruta de inicio de sesión
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()  # Buscar al usuario
        if user and user.check_password(form.password.data):  # Verificar si la contraseña es correcta
            login_user(user)  # Iniciar sesión
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('ventas.dashboard'))  # Redirige al dashboard de ventas
        flash('Credenciales incorrectas', 'danger')
    return render_template('auth/login.html', form=form)  # Mostrar el formulario de login

# Ruta para cerrar sesión
@auth.route('/logout')
@login_required  # Solo los usuarios autenticados pueden acceder
def logout():
    logout_user()  # Termina la sesión del usuario actual
    flash('Has cerrado sesión.', 'info')  # Muestra un mensaje flash
    return redirect(url_for('auth.login'))  # Redirige al formulario de login
