import unittest
from modelo.Usuario import Usuario
from modelo.Proyecto import Proyecto
from datetime import datetime, date,timedelta
from basededatos.conexion import Conexion

class TestUsuario(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base_de_datos="basededatos/greenscape.db"
        cls.conexion = Conexion(base_de_datos)
        cls.conexion.crear_base()
    
    def test_crear_proyecto(self):
        proyecto= Proyecto(1,"Jardin de paco","Podar plantas todo el tiempo",datetime(2024,11,7).date(),datetime(2024,12,31).date())
        self.assertTrue(Usuario.crear_proyecto(proyecto, self.conexion))

    def test_proyecto_none(self):
        resultado = Usuario.crear_proyecto(None, self.conexion)
        self.assertFalse(resultado)

    def test_proyecto_nombre_vacio(self):
        proyecto = Proyecto(2, "", "Descripción válida", datetime(2024, 11, 4).date(), datetime(2024, 12, 31).date())
        resultado = Usuario.crear_proyecto(proyecto, self.conexion)
        self.assertFalse(resultado)

    def test_proyecto_descripcion_vacia(self):
        proyecto = Proyecto(3, "Nombre válido", "    ", datetime(2024, 11, 4).date(), datetime(2024, 12, 31).date())
        resultado = Usuario.crear_proyecto(proyecto, self.conexion)
        self.assertFalse(resultado)

    def test_fecha_inicio_invalida(self):
        proyecto = Proyecto(4, "Nombre válido", "Descripción válida", "2024-11-04", datetime(2024, 12, 31).date())
        resultado = Usuario.crear_proyecto(proyecto, self.conexion)
        self.assertFalse(resultado)

    def test_fecha_final_invalida(self):
        proyecto = Proyecto(5, "Nombre válido", "Descripción válida", datetime(2024, 11, 4).date(), "2024-12-31")
        resultado = Usuario.crear_proyecto(proyecto, self.conexion)
        self.assertFalse(resultado)
    
    def test_fecha_inicio_antes_de_hoy(self):

        fecha_hoy = datetime.today().date()
        fecha_inicio_pasada = fecha_hoy - timedelta(days=1)  
        proyecto = Proyecto(1, "Nombre válido", "Descripción válida", fecha_inicio_pasada, fecha_hoy)
        resultado = Usuario.crear_proyecto(proyecto, self.conexion)
        self.assertFalse(resultado)

    @classmethod
    def tearDownClass(cls):
        cls.conexion.cerrar_conexion()
        
if __name__ == "__main__":
    unittest.main()