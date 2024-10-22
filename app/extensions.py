from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager



# Creamos una instancia llamada "db" la cual nos ayudará a establecer conexión
# con la base de datos
db = SQLAlchemy()


# Creamos una clase llamada "jwt" la cual nos ayudará a manejar todos los tokens que pasen por
# nuestra API
jwt = JWTManager()