from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from .forms import LoginForm
from . import auth  # Importa el blueprint desde __init__.py

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Lógica de autenticación aquí
        flash('Inicio de sesión exitoso', 'success')
        return redirect(url_for('home'))
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('auth.login'))
