from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from .forms import RegistrarVentaForm
from .models import Venta
from app.extensions import db
from . import ventas

@ventas.route('/dashboard')
@login_required
def dashboard():
    ventas = Venta.query.all()
    return render_template('ventas/dashboard.html', ventas=ventas)

@ventas.route('/registrar', methods=['GET', 'POST'])
@login_required
def registrar():
    form = RegistrarVentaForm()
    if form.validate_on_submit():
        nueva_venta = Venta(
            producto=form.producto.data,
            cantidad=form.cantidad.data,
            total=form.total.data
        )
        db.session.add(nueva_venta)
        db.session.commit()
        flash('Venta registrada exitosamente', 'success')
        return redirect(url_for('ventas.dashboard'))
    return render_template('ventas/registrar.html', form=form)
