class Tarea:
    def __init__(self, id_tarea, descripcion, estado, fecha_inicio, fecha_fin):
        self._id_tarea = id_tarea
        self._descripcion = descripcion
        self._estado = estado
        self._fecha_inicio = fecha_inicio
        self._fecha_fin = fecha_fin

   
    @property
    def id_tarea(self):
        return self._id_tarea

    @id_tarea.setter
    def id_tarea(self, id_tarea):
        self._id_tarea = id_tarea

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    
    @property
    def fecha_inicio(self):
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self._fecha_inicio = fecha_inicio

 
    @property
    def fecha_fin(self):
        return self._fecha_fin

    @fecha_fin.setter
    def fecha_fin(self, fecha_fin):
        self._fecha_fin = fecha_fin

    def __str__(self):
        return f"ID: {self.id_tarea}, Descripción: {self.descripcion}, Estado: {self.estado}, Fecha de Inicio: {self.fecha_inicio}, Fecha de Fin: {self.fecha_fin}"
