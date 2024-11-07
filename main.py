from flask import Flask, render_template, request, redirect, url_for,session
from basededatos.conexion import Conexion
from modelo.Usuario import Usuario
from modelo.Proyecto import Proyecto
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'una_clave_secreta_unica_y_segura'

@app.route('/', methods=['GET', 'POST'])
def index():
    usuario_s = session.get('usuario', {})
    if usuario_s:
        tipo_usuario_s = usuario_s.get('tipo_usuario')
        if tipo_usuario_s == 'Jardinero':
            return render_template('MenuJardinero.html', usuario=usuario_s)
        elif tipo_usuario_s == 'Administrador':
            return render_template('MenuAdmin.html', usuario=usuario_s)
    

    base_de_datos = ".venv/basededatos/greenscape.db"
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

                # Redirigir al menú adecuado según el tipo de usuario
                if tipo_usuario == "Jardinero":
                    conexion.cerrar_conexion()
                    return render_template('MenuJardinero.html', usuario=usuario_obj)
                else:
                    conexion.cerrar_conexion()
                    return render_template('MenuAdmin.html', usuario=usuario_obj)
        
        conexion.cerrar_conexion()
        return render_template('index.html', mensaje="Credenciales Invalidas")

    return render_template('index.html', mensaje="")

@app.route('/crearproyecto', methods=['GET', 'POST'])
def crear_proyecto():
    usuario = session.get('usuario', {})
    if not usuario:
        return redirect(url_for('index'))

    base_de_datos = ".venv/basededatos/greenscape.db"
    conexion = Conexion(base_de_datos)
    usuario_obj = conexion.buscar_usuario_por_id(usuario.get('id', None))
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        fecha_inicio = datetime.strptime(request.form['fecha_inicio'], '%Y-%m-%d').date()  
        fecha_final = datetime.strptime(request.form['fecha_final'], '%Y-%m-%d').date()

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

    return render_template('formularioCrearProyecto.html', usuario=usuario_obj)

@app.route('/resultado', methods=['GET', 'POST'])
def resultado():
    # Verificar si la sesión existe antes de mostrar el resultado
    if 'resultado' not in session:
        return redirect(url_for('index'))  

    resultado = session['resultado']
    session.pop('resultado', None)  # Limpiar el resultado de la sesión para no mantenerlo
    return render_template('resultado.html', resultado=resultado)
