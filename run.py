from app import create_app

# Crear la aplicación
app = create_app()

# Ejecutar el servidor Flask
if __name__ == "__main__":
    app.run(debug=True)  # Habilita el modo debug para ver los errores y recargar automáticamente
