class Planta:
    def __init__(self, id_planta, nombre, especie, requiere_cuidado,id_proyecto):
        self._id_planta = id_planta
        self._nombre = nombre
        self._especie = especie
        self._requiere_cuidado = requiere_cuidado
        self._id_proyecto=id_proyecto
        

    @property
    def id_proyecto(self):
        return self._id_proyecto
    
    @id_proyecto.setter
    def id_proyecto(self,id_proyecto):
        self._id_proyecto=id_proyecto

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
    def especie(self):
        return self._especie

    @especie.setter
    def especie(self, especie):
        self._especie = especie

 
    @property
    def requiere_cuidado(self):
        return self._requiere_cuidado

    @requiere_cuidado.setter
    def requiere_cuidado(self, requiere_cuidado):
        self._requiere_cuidado = requiere_cuidado

    def agregar_cuidado(self, cuidado):
        self._requiere_cuidado.append(cuidado)

    def __str__(self):
        return f"ID: {self.id_planta}, Nombre: {self.nombre}, especie: {self.especie}, requiere_cuidado: {self.requiere_cuidado}"
