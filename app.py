## @file app.py
#  @brief Componente principal de la aplicación Flask.
from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def hello():
    """!
    Endpoint para saludar al usuario.

    Parámetros:
    name (str): nombre del usurio pasado como parámetro en la URL.

    Retorna:
    str: mensaje de saludo personalizado.
    """
    name = request.args.get('name')
    return f"Hello, {name}!"

if __name__ == '__main__':
    """!Se desactiva el modo debug para evitar la ejecución de código arbitrario en producción."""
    app.run(debug=False, host='0.0.0.0', port=5000)