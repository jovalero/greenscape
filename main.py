from flask import Flask, render_template, request, redirect, url_for, session
from basededatos.conexion import Conexion
from modelo.Usuario import Usuario
from modelo.Proyecto import Proyecto
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'una_clave_secreta_unica_y_segura'  # Asegúrate de que sea una clave larga y segura


@app.route('/', methods=['GET', 'POST'])
def home():
    session.clear()
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def index():

    if 'usuario' in session:
        if session['usuario']['tipo_usuario'] == "Jardinero":
            return redirect(url_for('menu_jardinero'))
        else:
            return redirect(url_for('menu_admin'))
        
    base_de_datos = "basededatos/greenscape.db"
    conexion = Conexion(base_de_datos)
    conexion.crear_base()
    usuarios = conexion.mostrar_usuarios()

    if request.method == 'POST':
        usuario_form = request.form['username']
        password_form = request.form['password']

        for usuario in usuarios:
            id_usuario, nombre, telefono, password, email, tipo_usuario = usuario

            if email == usuario_form and password == password_form:
                usuario_obj = Usuario(id_usuario, nombre, password, email, tipo_usuario, telefono)
                session['usuario'] = {'nombre': usuario_obj.nombre, 'id': usuario_obj.id_usuario, 'tipo_usuario': usuario_obj.tipo_usuario}
                if tipo_usuario == "Jardinero":
                    conexion.cerrar_conexion()
                    return redirect(url_for('menu_jardinero'))
                else:
                    conexion.cerrar_conexion()
                    return redirect(url_for('menu_admin'))
        conexion.cerrar_conexion()
        return render_template('index.html', mensaje="Credenciales Invalidas")

    return render_template('index.html', mensaje="")

@app.route('/menu_jardinero')
def menu_jardinero():
    if 'usuario' not in session:
        return redirect(url_for('index'))
    usuario = session['usuario']
    return render_template('MenuJardinero.html', usuario=usuario)

@app.route('/menu_admin')
def menu_admin():
    if 'usuario' not in session:
        return redirect(url_for('index'))
    usuario = session['usuario']
    menu=request.args.get('menu')

    if menu:
        if menu=='proyectos':
            base_de_datos = "basededatos/greenscape.db"
            conexion = Conexion(base_de_datos)
            Proyectos=conexion.mostrar_proyectos()
            proyectos_objetos = []
            for proyecto in Proyectos:
                proyecto_objeto = Proyecto(
                id_proyecto=proyecto[0],
                nombre=proyecto[1],
                descripcion=proyecto[2],
                fecha_inicio=proyecto[3],
                fecha_final=proyecto[4]) 
                proyectos_objetos.append(proyecto_objeto)
                       
            return render_template('menu_proyectos.html',usuario=usuario, proyectos=proyectos_objetos)
        elif menu == 'jardineros':
            return render_template('menu_gestion_jardineros.html',usuario=usuario)

    return render_template('MenuAdmin.html', usuario=usuario)

@app.route('/formulariosproyectos', methods=['GET', 'POST'])
def crear_proyecto():
     # Verificación de permisos de usuario
    usuario = session.get('usuario', {})
    if not usuario or usuario.get('tipo_usuario') != "Admin":
        return redirect(url_for('index'))

    base_de_datos = "basededatos/greenscape.db"
    conexion = Conexion(base_de_datos)
    usuario_obj = conexion.buscar_usuario_por_id(usuario.get('id', None))

    proyecto_objeto = None  # Inicializamos la variable para pasarla al formulario
    
    # Verificar si estamos editando un proyecto existente
    id_p = request.args.get('id')
    if id_p:
        # Cargar proyecto existente en base al ID
        proyectos = conexion.mostrar_proyectos()
        for proyecto in proyectos:
            if proyecto[0] == int(id_p):
                proyecto_objeto = Proyecto(
                    id_proyecto=proyecto[0],
                    nombre=proyecto[1],
                    descripcion=proyecto[2],
                    fecha_inicio=proyecto[3],
                    fecha_final=proyecto[4]
                )
                break

   
    if request.method == 'POST':
        id_proyecto = request.form.get('id_proyecto')
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        fecha_inicio = datetime.strptime(request.form['fecha_inicio'], '%Y-%m-%d').date()
        fecha_final = datetime.strptime(request.form['fecha_final'], '%Y-%m-%d').date()

        if id_proyecto:
            proyecto_objeto = Proyecto(
                id_proyecto=int(id_proyecto),
                nombre=nombre,
                descripcion=descripcion,
                fecha_inicio=fecha_inicio,
                fecha_final=fecha_final
            )
            resultado = usuario_obj.modificar_proyecto(proyecto_objeto, conexion)
        else:
            
            nuevo_proyecto = Proyecto(
                id_proyecto=None,
                nombre=nombre,
                descripcion=descripcion,
                fecha_inicio=fecha_inicio,
                fecha_final=fecha_final
            )
            resultado = usuario_obj.crear_proyecto(nuevo_proyecto, conexion)

        session['resultado'] = resultado
        return redirect(url_for('resultado'))

    return render_template('formularioProyectos.html', usuario=usuario_obj, proyecto=proyecto_objeto)

@app.route('/eliminarproyecto', methods=['GET', 'POST'])
def eliminarproyecto():
    

@app.route('/resultado', methods=['GET', 'POST'])
def resultado():

    if 'resultado' not in session:
        return redirect(url_for('index'))  

    resultado = session['resultado']
    session.pop('resultado', None)  
    return render_template('resultado.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
