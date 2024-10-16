# Se va encargar de montar el servidor
# flask es la librería
# Flask (con F mayúscula es el módulo)
from flask import Flask # <- Nos permite crear el servior
from flask_restful import Api # <- Crear la funcionalidad de API

# Cuando queramos importar un archivo usamos un .
from .routes import APIRoutes

# Desde el archivo config importamos la clase "Config"
from .config import Config


# Desde el archivo extensions importamos la variable "db"
from .extensions import db

# Creamos una función que configure el servidor
def configurar_app():
  # Va a almacenar el servidor
  app = Flask(__name__)

  # Le indico a mi app que como archivo de configuración utilice config
  app.config.from_object(Config)

  # Le decimos a mi base de datos que se va a inicializar en nuestra app
  db.init_app(app)

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


  return app
