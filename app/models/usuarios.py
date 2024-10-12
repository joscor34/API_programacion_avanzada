# Importamos la variable que hace referencia a mi base de datos
from app.extensions import db

from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
  __tablename__ = 'usuarios' # <- Indica a que tabla hace referencia este modelo
  id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String, nullable=False)
  email = db.Column(db.String, nullable=False)
  telefono = db.Column(db.String, nullable=False)
  password = db.Column(db.Text(), nullable=False)

  # La contraseña que nos manda el usuario, le llega a la función "generate_password_hash"
  # esta función, encripta la contraseña y el hash creado lo guarda en el atributo "password"
  # que es el que le llega a la BD
  def hashear_password(self, password):
    self.password = generate_password_hash(password)


  # Esta función recibe la contraseña en texto plano y la compara con el has que está almacenado
  # en la DB, si coincide nos regresa un True, sino nos regresa un False
  def verificar_password(self, password):
    return check_password_hash(self.password, password)


  # Método de la clase User
  def save(self):
    # Crea una sesión con mi base de datos 
    db.session.add(self)

    # En esa conexión guardamos los cambios y la cerramos
    db.session.commit()



  def delete(self):
    # Abre una sesión con mi DB
    db.session.delete(self)

    # Se guardan los cambios y se cierra la conexión
    db.session.commit()