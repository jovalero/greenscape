class Jardinero:
    def __init__(self, id_jardinero, nombre, experiencia):
        self._id_jardinero = id_jardinero
        self._nombre = nombre
        self._experiencia = experiencia
        self._tareas_asignadas = []

 
    @property
    def id_jardinero(self):
        return self._id_jardinero

    @id_jardinero.setter
    def id_jardinero(self, id_jardinero):
        self._id_jardinero = id_jardinero


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

   
    @property
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def experiencia(self, experiencia):
        self._experiencia = experiencia

    
    @property
    def tareas_asignadas(self):
        return self._tareas_asignadas

    @tareas_asignadas.setter
    def tareas_asignadas(self, tareas):
        if isinstance(tareas, list):
            self._tareas_asignadas = tareas
        else:
            raise ValueError("Las tareas asignadas deben ser una lista")

    def asignar_tarea(self, tarea):
        self._tareas_asignadas.append(tarea)

    def __str__(self):
        return f"ID: {self.id_jardinero}, Nombre: {self.nombre}, Experiencia: {self.experiencia}, Tareas Asignadas: {self.tareas_asignadas}"
