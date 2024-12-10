from app.extensions import db

class Venta(db.Model):
    __tablename__ = 'venta'
    __table_args__ = {'extend_existing': True}  # Evitar el error de tabla duplicada

    id = db.Column(db.Integer, primary_key=True)
    producto = db.Column(db.String(120), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Venta {self.producto} - {self.cantidad}>'
