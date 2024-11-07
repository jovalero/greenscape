from basededatos.conexion import Conexion
from modelo.Proyecto import Proyecto
from datetime import datetime, date

class Usuario:
    def __init__(self, id_usuario, nombre, password,email,tipo_usuario,telefono):
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._password = password
        self._email = email
        self._tipo_usuario=tipo_usuario
        self._telefono=telefono

    @property
    def telefono(self):
        return telefono
    
    @telefono.setter
    def telefono(self, telefono):
        self._telefono= telefono
    @property
    def tipo_usuario(self):
        return self._tipo_usuario
    
    @tipo_usuario.setter
    def tipo_usuario(self,tipo_usuario):
        self._tipo_usuario=tipo_usuario
 
    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

   
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
            self._email = email


    def __str__(self):
        return f"ID: {self.id_usuario}, Nombre: {self.nombre}, password: {self.password}, email: {self.email}, tipo de usuario: {self.tipo_usuario}"

    def crear_proyecto(self,proyecto: Proyecto, conexion: Conexion):
        flag = False
        if proyecto is not None:
            if proyecto.descripcion.strip() and proyecto.nombre.strip():
                if isinstance(proyecto.fecha_inicio, (datetime, date)) and isinstance(proyecto.fecha_final, (datetime, date)):
                    if proyecto.fecha_inicio >= datetime.now().date() and proyecto.fecha_inicio <= proyecto.fecha_final:  
                        conexion.insertar_proyecto(proyecto.nombre, proyecto.descripcion, proyecto.fecha_inicio, proyecto.fecha_final)
                        flag = True
        return flag
        