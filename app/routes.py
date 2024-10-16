# En el archivo routes nosotros vamos a tener las rutas (paths)
# que el servidor va a poder manejar

from flask_restful import Resource
from flask import request #<- Nos permite interceptar la info del usuario

from .methods import user_register
from .methods import user_login

# Creamos un recurso que nuestra aplicación puede cargar (METODO)
class HolaMundo(Resource):
  # Este método se ejecuta cuando el usuario lo llama con un GET
  def get(self):
    return {'Mensaje': 'Hola mundo desde GET'}

  def post(self):
    
    return {'Mensaje': 'Hola mundo desde POST'}

class Registro(Resource):
  # Como el usuario envia información utilizamos un post
  def post(self):
    # Información que el usario envia a través del post
    user_info = request.form

    username = user_info.get('nombre')
    email = user_info.get('correo')
    password = user_info.get('password')
    telefono = user_info.get('telefono')

    respuesta, status = user_register(username, email, telefono, password)    

    return respuesta, status


# Van a crear un recurso para el login, le van a asigar una ruta y su servidor tiene que recibir
# la siguiente información del cliente: "correo" y "contraseña"
class Login(Resource):
  # Como el usuario envia información utilizamos un post
  def post(self):
    # Información que el usario envia a través del post
    user_info = request.form

    email = user_info.get('correo')
    password = user_info.get('password')

    respuesta, status = user_login(email, password)

    return respuesta, status




# Simplemente se va a encargar de darle rutas a mis recursos
class APIRoutes:
  def init_api(self, api):
    api.add_resource(HolaMundo, '/')
    api.add_resource(Registro, '/registro')
    api.add_resource(Login, '/login')


# La ruta "/" <- ruta Raíz 