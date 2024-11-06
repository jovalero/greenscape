class Planta:
    def __init__(self, id_planta, nombre, tipo, cuidados):
        self._id_planta = id_planta
        self._nombre = nombre
        self._tipo = tipo
        self._cuidados = cuidados

    @property
    def id_planta(self):
        return self._id_planta

    @id_planta.setter
    def id_planta(self, id_planta):
        self._id_planta = id_planta

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre


    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

 
    @property
    def cuidados(self):
        return self._cuidados

    @cuidados.setter
    def cuidados(self, cuidados):
        if isinstance(cuidados, list):
            self._cuidados = cuidados
        else:
            raise ValueError("Cuidados debe ser una lista")

    def agregar_cuidado(self, cuidado):
        self._cuidados.append(cuidado)

    def __str__(self):
        return f"ID: {self.id_planta}, Nombre: {self.nombre}, Tipo: {self.tipo}, Cuidados: {self.cuidados}"
