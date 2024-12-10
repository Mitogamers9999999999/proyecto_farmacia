from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class RegistrarVentaForm(FlaskForm):
    producto = StringField('Producto', validators=[DataRequired()])
    cantidad = IntegerField('Cantidad', validators=[DataRequired(), NumberRange(min=1)])
    total = FloatField('Total', validators=[DataRequired()])
    submit = SubmitField('Registrar Venta')
