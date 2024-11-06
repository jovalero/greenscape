from modelo import Cuidado,Jardinero,Planta,Proyecto,Tarea
from basededatos.conexion import Conexion

base_datos="basededatos/greenscape.db"
conexion=Conexion(base_datos)

conexion.crear_base()
conexion.cerrar_conexion
jardineros = []
proyectos = []
tareas = []
plantas = []

def menu():
    print("=== Menú de Opciones ===")
    print("1. Crear Jardinero")
    print("2. Crear Proyecto de Jardinería")
    print("3. Crear Tarea")
    print("4. Crear Planta")
    print("5. Ver Historial")
    print("6. Salir")
    return input("Selecciona una opción: ")

def crear_jardinero():
    id_jardinero = int(input("ID del Jardinero: "))
    nombre = input("Nombre del Jardinero: ")
    experiencia = input("Experiencia del Jardinero: ")
    jardinero = Jardinero(id_jardinero, nombre, experiencia)
    jardineros.append(jardinero)
    print(f"Jardinero {nombre} creado con éxito.\n")

def crear_proyecto():
    id_proyecto = int(input("ID del Proyecto: "))
    nombre = input("Nombre del Proyecto: ")
    descripcion = input("Descripción del Proyecto: ")
    proyecto = Proyecto(id_proyecto, nombre, descripcion)
    proyectos.append(proyecto)
    print(f"Proyecto {nombre} creado con éxito.\n")

def crear_tarea():
    id_tarea = int(input("ID de la Tarea: "))
    descripcion = input("Descripción de la Tarea: ")
    estado = input("Estado de la Tarea (pendiente/en progreso/completada): ")
    fecha_inicio = input("Fecha de Inicio (YYYY-MM-DD): ")
    fecha_fin = input("Fecha de Fin (YYYY-MM-DD): ")
    tarea = Tarea(id_tarea, descripcion, estado, fecha_inicio, fecha_fin)
    tareas.append(tarea)
    print(f"Tarea '{descripcion}' creada con éxito.\n")

def crear_planta():
    id_planta = int(input("ID de la Planta: "))
    nombre = input("Nombre de la Planta: ")
    tipo = input("Tipo de Planta: ")
    planta = Planta(id_planta, nombre, tipo, [])
    plantas.append(planta)
    print(f"Planta {nombre} creada con éxito.\n")

def ver_historial():
    print("\n=== Historial de Entidades ===")
    print("Jardineros:")
    for jardinero in jardineros:
        print(jardinero)
    
    print("\nProyectos de Jardinería:")
    for proyecto in proyectos:
        print(proyecto)
    
    print("\nTareas:")
    for tarea in tareas:
        print(tarea)
    
    print("\nPlantas:")
    for planta in plantas:
        print(planta)
    print("\n")


while True:
    opcion = menu()
    
    if opcion == "1":
        crear_jardinero()
    elif opcion == "2":
        crear_proyecto()
    elif opcion == "3":
        crear_tarea()
    elif opcion == "4":
        crear_planta()
    elif opcion == "5":
        ver_historial()
    elif opcion == "6":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
