from flask import Blueprint,render_template,redirect,request
from icebreaker2.modulos.empleados.model.empleados import Empleado
from icebreaker2.modulos import db
from flask import flash
from flask import session


bp_emp = Blueprint('empleados', __name__)
print(Empleado)


@bp_emp.route('/empleados/')
def empleados():
    cdx={
        "empleados":Empleado.query.all()
    }

    return render_template('empleados/empleados.html',cdx=cdx)

@bp_emp.route('/empleados/login')
def empleados_login():

    return render_template('empleados/login.html')


@bp_emp.route('/empleados/login', methods=['GET', 'POST'])
def empleados_login_alta():
    cdx = {
        "empleados": Empleado.query.all()
    }
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'administracion' and password == 'contraseña':
            #Autenticación exitosa
            session['username'] = username  # Guardar el nombre de usuario en la sesión
            return render_template('empleados/empleados.html',cdx=cdx)
        else:
            flash('Nombre de usuario o contraseña incorrectos')
            return render_template('empleados/login.html')

@bp_emp.route('/empleados/logout')
def empleados_logout():
    # Eliminar el nombre de usuario de la sesión
    session.pop('username', None)
    return render_template('empleados/login.html')

@bp_emp.route('/empleados/alta',methods=['GET','POST'])
def empleados_alta():
    if request.method == 'GET':
        cdx={
            "tipo":"alta",
            "empleado":Empleado.query.filter_by(id=id).first()
        }

        return render_template('empleados/ABC_Empleados.html',cdx=cdx)
    elif request.method == 'POST':
        nombre= request.form.get('nombre')
        apellido = request.form.get('apellido')
        fecha = request.form.get('fecha-input')
        fecha = str(fecha)
        monto = request.form.get('monto')
        monto = monto.replace('$','')
        monto = monto.replace(',', '')
        monto = float(monto)
        celular = request.form.get('celular')
        comentarios = request.form.get('comentarios')
        e = Empleado(
            nombre=nombre,
            apellido=apellido,
            fecha=fecha,
            monto=monto,
            comentarios=comentarios,
            celular=celular
        )
        db.session.add(e)
        db.session.commit()
        return redirect('/empleados/')
        return "POST"
    else:
        return "ERROR"

@bp_emp.route('/empleados/comentarios/<int:id>')
def comentarios(id):

    empleado = Empleado.query.filter_by(id=id).first()
    return empleado.comentarios

@bp_emp.route('/empleados/borrar/<int:id>',methods=['GET','POST'])
def borrar(id):
    if request.method == 'GET':
        cdx={
            "tipo":"borrar",
            "empleado":Empleado.query.filter_by(id=id).first()
        }
        return render_template('empleados/ABC_Empleados.html',cdx=cdx)

    elif request.method == 'POST':
        e = Empleado.query.filter_by(id=id).first()
        db.session.delete(e)
        db.session.commit()
        return redirect('/empleados/')
    else:
        return "ERROR"


@bp_emp.route('/empleados/editar/<int:id>',methods=['GET','POST'])
def editar(id):
    if request.method == 'GET':
        cdx={
            "tipo":"editar",
            "empleado":Empleado.query.filter_by(id=id).first()
        }

        return render_template('empleados/ABC_Empleados.html',cdx=cdx)

    elif request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        fecha=request.form.get('fecha-input')
        monto = request.form.get('monto')
        monto = monto.replace('$','')
        monto = monto.replace(',','')
        monto = float(monto)
        comentarios = request.form.get('comentarios')
        celular = request.form.get('celular')
        e=Empleado.query.filter_by(id=id).first()
        e.nombre=nombre
        e.apellido=apellido
        e.fecha=fecha
        e.monto=monto
        e.comentarios=comentarios
        e.celular=celular
        db.session.add(e)
        db.session.commit()
        return redirect("/empleados/")

    else:
        return "ERROR"

@bp_emp.app_template_filter('formato_moneda')
def formato_moneda(numero:float):
    cadena ="0.00"
    if(numero):
        cadena = f"${numero:0,.2f}"
    else:
        cadena = "Finalizado"
    return cadena

