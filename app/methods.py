# Ejecuta todas las peticiones que se hagan a la base datos


from app.models.usuarios import User

def user_register(nombre, email, telefono, password):
  

  usuario_existente = User.query.filter_by(email=email).first()

  print(usuario_existente)

  if usuario_existente is not None:
    return {'Error': 'El usuario ya está registrado :('}, 403

  # Creamos un objeto de tipo User con los valores que el cliente solicitó
  nuevo_usuario = User(nombre=nombre, email=email, telefono=telefono)

  # Este método lo que hace es recibir la pass en texto plano, hashearla y guardarla dentro 
  # de nuestro objeto
  nuevo_usuario.hashear_password(password=password)

  # Invocamos el método Save que se encargar de hacer todo el proceso para
  # guardarlo en mi DB
  nuevo_usuario.save()

  return {
    'status': 'Usuario registrado',
    'email': email,
    'telefono': telefono
  }, 200