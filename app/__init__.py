# Se va encargar de montar el servidor
# flask es la librería
# Flask (con F mayúscula es el módulo)
from flask import Flask, jsonify # <- Nos permite crear el servior
from flask_restful import Api # <- Crear la funcionalidad de API

# Cuando queramos importar un archivo usamos un .
from .routes import APIRoutes

# Desde el archivo config importamos la clase "Config"
from .config import Config

from flask_jwt_extended.exceptions import NoAuthorizationError, InvalidHeaderError


# Desde el archivo extensions importamos la variable "db"
from .extensions import db, jwt


# Creamos una función que configure el servidor
def configurar_app():
  # Va a almacenar el servidor
  app = Flask(__name__)

  # Le indico a mi app que como archivo de configuración utilice config
  app.config.from_object(Config)

  # Le decimos a mi base de datos que se va a inicializar en nuestra app
  db.init_app(app)

  # Le dicmos a JWT que se va a inicializar en nuestra app
  jwt.init_app(app)


  # Se ejecuta mientras el servidor se está montado
  with app.app_context():

    # Inicializa todas las tablas de nuestra base de datos
    db.create_all()


  # Variable que a almacenar la API
  # Le indicamos sobre que servidor va a interactuar
  api = Api(app)

  # Configuramos las rutas y los recursos
  rutas = APIRoutes()
  rutas.init_api(api)

  # Manejador para cuando no se proporciona un token
  @app.errorhandler(NoAuthorizationError)
  def handle_no_token(e):
      return jsonify({
          "message": "Se requiere un token de autorización.",
          "error": str(e)
      }), 401

  # Manejador para cuando el token es inválido o tiene un formato incorrecto
  @app.errorhandler(InvalidHeaderError)
  def handle_invalid_token(e):
      return jsonify({
          "message": "Token inválido o mal formado.",
          "error": str(e)
      }), 422

  # Manejador para cuando el token ha expirado
  @jwt.expired_token_loader
  def expired_token_callback(jwt_header, jwt_payload):
      return jsonify({
          "message": "El token ha expirado.",
          "error": "token_expired"
      }), 401




  return app
