class Cuidado:
    def __init__(self, id_cuidado, descripcion, frecuencia):
        self._id_cuidado = id_cuidado
        self._descripcion = descripcion
        self._frecuencia = frecuencia
    
    @property
    def id_cuidado(self):
        return self._id_cuidado
    
    @id_cuidado.setter
    def id_cuidado(self, id_cuidado):
        self._id_cuidado=id_cuidado

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion=descripcion

    @property
    def frecuencia(self):
        return self._frecuencia

    @frecuencia.setter
    def frecuencia(self, frecuencia):
        self._frecuencia=frecuencia

    def __str__(self) -> str:
        return f"ID:{self._id_cuidado}, Descripcion:{self.descripcion}, Frecuencia:{self.frecuencia}"