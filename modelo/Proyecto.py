class Proyecto:
    def __init__(self, id_proyecto, nombre, descripcion,fecha_inicio,fecha_final):
        self._id_proyecto = id_proyecto
        self._nombre = nombre
        self._descripcion = descripcion
        self._fecha_inicio = fecha_inicio
        self._fecha_final = fecha_final

   
    @property
    def id_proyecto(self):
        return self._id_proyecto

    @id_proyecto.setter
    def id_proyecto(self, id_proyecto):
        self._id_proyecto = id_proyecto

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

   
    @property
    def fecha_inicio(self):
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self._fecha_inicio = fecha_inicio

   
    @property
    def fecha_final(self):
        return self._fecha_final

    @fecha_final.setter
    def fecha_final(self, fecha_final):
        self._fecha_final = fecha_final

   
    def registrar_actividad(self, actividad):
        self._fecha_final.append(actividad)

    def __str__(self):
        return f"ID: {self.id_proyecto}, Nombre: {self.nombre}, Descripción: {self.descripcion}, fecha_inicio: {self.fecha_inicio}, Registro de fecha_final: {self.fecha_final}"
