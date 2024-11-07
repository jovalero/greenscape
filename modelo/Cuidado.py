class Cuidado:
    def __init__(self, id_cuidado, descripcion, tipo_cuidado,fecha,id_planta):
        self._id_cuidado = id_cuidado
        self._descripcion = descripcion
        self._tipo_cuidado = tipo_cuidado
        self._fecha=fecha
        self._id_planta=id_planta
    
    @property
    def id_planta(self):
        return self._id_planta
    
    @id_planta.setter
    def id_planta(self,id_planta):
        self._id_planta=id_planta
        
    @property
    def fecha(self):
        return self._fecha
    
    @fecha.seterr
    def fecha(self,fecha):
        self.fecha=fecha
    
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
    def tipo_cuidado(self):
        return self._tipo_cuidado

    @tipo_cuidado.setter
    def tipo_cuidado(self, tipo_cuidado):
        self._tipo_cuidado=tipo_cuidado

    def __str__(self) -> str:
        return f"ID:{self._id_cuidado}, Descripcion:{self.descripcion}, tipo_cuidado:{self.tipo_cuidado}"