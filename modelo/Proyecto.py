class Proyecto:
    def __init__(self, id_proyecto, nombre, descripcion):
        self._id_proyecto = id_proyecto
        self._nombre = nombre
        self._descripcion = descripcion
        self._tareas = []
        self._registro_actividades = []

   
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
    def tareas(self):
        return self._tareas

    @tareas.setter
    def tareas(self, tareas):
        if isinstance(tareas, list):
            self._tareas = tareas
        else:
            raise ValueError("Tareas debe ser una lista")

   
    @property
    def registro_actividades(self):
        return self._registro_actividades

    @registro_actividades.setter
    def registro_actividades(self, actividades):
        if isinstance(actividades, list):
            self._registro_actividades = actividades
        else:
            raise ValueError("Registro de actividades debe ser una lista")

   
    def registrar_actividad(self, actividad):
        self._registro_actividades.append(actividad)

    def __str__(self):
        return f"ID: {self.id_proyecto}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Tareas: {self.tareas}, Registro de Actividades: {self.registro_actividades}"
