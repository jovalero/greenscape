import sqlite3

class Conexion:
    def __init__(self,nombre):
        self.nombre_bd=nombre
        self.conexion=sqlite3.connect(self.nombre_bd)
        self.cursor=self.conexion.cursor()
    
    def crear_tabla_proyecto(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS proyecto(id_proyecto INTEGER PRIMARY KEY, nombre TEXT, descripcion TEXT, fecha_inicio DATE, fecha_final DATE)")
        self.conexion.commit()

    ##CRUD PROYECTO
    def insertar_proyecto(self, nombre, descripcion, fecha_inicio, fecha_final):
        self.cursor.execute("""
            INSERT INTO proyecto (nombre, descripcion, fecha_inicio, fecha_final)
            VALUES (?, ?, ?, ?)
        """, (nombre, descripcion, fecha_inicio, fecha_final))
        self.conexion.commit()

    def editar_proyecto(self, id_proyecto, nombre, descripcion, fecha_inicio, fecha_final):
        self.cursor.execute("""
            UPDATE proyecto
            SET nombre = ?, descripcion = ?, fecha_inicio = ?, fecha_final = ?
            WHERE id_proyecto = ?
        """, (nombre, descripcion, fecha_inicio, fecha_final, id_proyecto))
        self.conexion.commit()

    def mostrar_proyectos(self):
        
        self.cursor.execute("SELECT id_proyecto, nombre, descripcion, fecha_inicio, fecha_final FROM proyecto")
        proyectos = self.cursor.fetchall()

        return proyectos
    
    def eliminar_proyecto(self, id_proyecto):

        self.cursor.execute("DELETE FROM proyecto WHERE id_proyecto = ?", (id_proyecto))
        self.conexion.commit()
    
    ##CRUD PROYECTO

    def crear_planta(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS planta(
                id_planta INTEGER PRIMARY KEY, 
                especie TEXT, 
                id_proyecto INTEGER, 
                requiere_cuidado BOOLEAN, 
                FOREIGN KEY (id_proyecto) REFERENCES proyecto(id)
            )
        """)
        self.conexion.commit()
    
    ##CRUD PLANTA

    def insertar_planta(self, especie, id_proyecto, requiere_cuidado):
        self.cursor.execute("""
            INSERT INTO planta (especie, id_proyecto, requiere_cuidado)
            VALUES (?, ?, ?)
        """, (especie, id_proyecto, requiere_cuidado))
        self.conexion.commit()

    def editar_planta(self, id_planta, especie, id_proyecto, requiere_cuidado):
        self.cursor.execute("""
            UPDATE planta
            SET especie = ?, id_proyecto = ?, requiere_cuidado = ?
            WHERE id_planta = ?
        """, (especie, id_proyecto, requiere_cuidado, id_planta))
        self.conexion.commit()

    def mostrar_plantas(self):
        self.cursor.execute("SELECT id_planta, especie, id_proyecto, requiere_cuidado FROM planta")
        plantas = self.cursor.fetchall()
        return plantas

    def eliminar_planta(self, id_planta):
        self.cursor.execute("DELETE FROM planta WHERE id_planta = ?", (id_planta,))
        self.conexion.commit()

    ##CRUD PLANTA   


    def crear_cuidado(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cuidado(
                id_cuidado INTEGER PRIMARY KEY, 
                descripcion TEXT, 
                id_planta INTEGER, 
                fecha DATE, 
                tipo_cuidado TEXT, 
                FOREIGN KEY (id_planta) REFERENCES planta(id_planta)
            )
        """)        
        self.conexion.commit()    

    ##CRUD CUIDADO

    def insertar_cuidado(self, descripcion, id_planta, fecha, tipo_cuidado):
        self.cursor.execute("""
            INSERT INTO cuidado (descripcion, id_planta, fecha, tipo_cuidado)
            VALUES (?, ?, ?, ?)
        """, (descripcion, id_planta, fecha, tipo_cuidado))
        self.conexion.commit()

    def editar_cuidado(self, id_cuidado, descripcion, id_planta, fecha, tipo_cuidado):
        self.cursor.execute("""
            UPDATE cuidado
            SET descripcion = ?, id_planta = ?, fecha = ?, tipo_cuidado = ?
            WHERE id_cuidado = ?
        """, (descripcion, id_planta, fecha, tipo_cuidado, id_cuidado))
        self.conexion.commit()

    def mostrar_cuidados(self):
        self.cursor.execute("SELECT id_cuidado, descripcion, id_planta, fecha, tipo_cuidado FROM cuidado")
        cuidados = self.cursor.fetchall()
        return cuidados

    def eliminar_cuidado(self, id_cuidado):
        self.cursor.execute("DELETE FROM cuidado WHERE id_cuidado = ?", (id_cuidado,))
        self.conexion.commit()

    
    ##CRUD CUIDADO

    def crear_tarea(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarea(
                id_tarea INTEGER PRIMARY KEY, 
                estado TEXT, 
                id_proyecto INTEGER, 
                fecha_inicio DATE, 
                fecha_venc DATE, 
                descripcion TEXT, 
                FOREIGN KEY (id_proyecto) REFERENCES proyecto(id_proyecto)
            )
        """)        
        self.conexion.commit()       
    
    ##CRUD TAREA
    def insertar_tarea(self, estado, id_proyecto, fecha_inicio, fecha_venc, descripcion):
        self.cursor.execute("""
            INSERT INTO tarea (estado, id_proyecto, fecha_inicio, fecha_venc, descripcion)
            VALUES (?, ?, ?, ?, ?)
        """, (estado, id_proyecto, fecha_inicio, fecha_venc, descripcion))
        self.conexion.commit()

    def editar_tarea(self, id_tarea, estado, id_proyecto, fecha_inicio, fecha_venc, descripcion):
        self.cursor.execute("""
            UPDATE tarea
            SET estado = ?, id_proyecto = ?, fecha_inicio = ?, fecha_venc = ?, descripcion = ?
            WHERE id_tarea = ?
        """, (estado, id_proyecto, fecha_inicio, fecha_venc, descripcion, id_tarea))
        self.conexion.commit()

    def mostrar_tareas(self):
        self.cursor.execute("SELECT id_tarea, estado, id_proyecto, fecha_inicio, fecha_venc, descripcion FROM tarea")
        tareas = self.cursor.fetchall()
        return tareas

    def eliminar_tarea(self, id_tarea):
        self.cursor.execute("DELETE FROM tarea WHERE id_tarea = ?", (id_tarea,))
        self.conexion.commit()
    
    ##CRUD TAREA
    def crear_usuario(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS usuario(id_usuario INTEGER PRIMARY KEY, nombre TEXT, telefono INTEGER, password TEXT, email TEXT, tipo_usuario TEXT)")
        self.conexion.commit() 

    #CRUD USUARIO

    def insertar_usuario(self, nombre, telefono, password, email, tipo_usuario):
        self.cursor.execute("""
            INSERT INTO usuario (nombre, telefono, password, email, tipo_usuario)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, telefono, password, email, tipo_usuario))
        self.conexion.commit()

    def editar_usuario(self, id_usuario, nombre, telefono, password, email, tipo_usuario):
        self.cursor.execute("""
            UPDATE usuario
            SET nombre = ?, telefono = ?, password = ?, email = ?, tipo_usuario = ?
            WHERE id_usuario = ?
        """, (nombre, telefono, password, email, tipo_usuario, id_usuario))
        self.conexion.commit()

    def mostrar_usuarios(self):
        self.cursor.execute("SELECT id_usuario, nombre, telefono, password, email, tipo_usuario FROM usuario")
        usuarios = self.cursor.fetchall()
        return usuarios

    def eliminar_usuario(self, id_usuario):
        self.cursor.execute("DELETE FROM usuario WHERE id_usuario = ?", (id_usuario,))
        self.conexion.commit()

    #CRUD USUARIO

    def crear_tarea_jardinero(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarea_jardinero (
                id_tarea_jardinero INTEGER PRIMARY KEY,
                id_usuario INTEGER,
                id_tarea INTEGER,
                FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
                FOREIGN KEY (id_tarea) REFERENCES tarea(id_tarea)
            )
        """)
        self.conexion.commit()

    #CRUD TAREA_JARDINERO
    def insertar_tarea_jardinero(self, id_usuario, id_tarea):
        self.cursor.execute("""
            INSERT INTO tarea_jardinero (id_usuario, id_tarea)
            VALUES (?, ?)
        """, (id_usuario, id_tarea))
        self.conexion.commit()

    def editar_tarea_jardinero(self, id_tarea_jardinero, id_usuario, id_tarea):
        self.cursor.execute("""
            UPDATE tarea_jardinero
            SET id_usuario = ?, id_tarea = ?
            WHERE id_tarea_jardinero = ?
        """, (id_usuario, id_tarea, id_tarea_jardinero))
        self.conexion.commit()

    def mostrar_tareas_jardinero(self):
        self.cursor.execute("SELECT id_tarea_jardinero, id_usuario, id_tarea FROM tarea_jardinero")
        tareas_jardinero = self.cursor.fetchall()
        return tareas_jardinero

    def eliminar_tarea_jardinero(self, id_tarea_jardinero):
        self.cursor.execute("DELETE FROM tarea_jardinero WHERE id_tarea_jardinero = ?", (id_tarea_jardinero,))
        self.conexion.commit()
    
    #CRUD TAREA_JARDINERO

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()

    def crear_base(self):
        self.crear_tabla_proyecto()
        self.crear_planta()
        self.crear_cuidado()
        self.crear_usuario()
        self.crear_tarea()
        self.crear_tarea_jardinero()