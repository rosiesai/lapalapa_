from flask import Blueprint,render_template,redirect,request
from icebreaker2.modulos.admin.model.admin import Admin
from icebreaker2.modulos import db
from flask import flash
from flask import session
from werkzeug.security import check_password_hash


bp_admin = Blueprint('admin', __name__)
print(Admin)


@bp_admin.route('/admin/')
def admin():
    cdx={
        "admin":Admin.query.all()
    }

    return render_template('admin/admin.html',cdx=cdx)


@bp_admin.route('/admin/alta',methods=['GET','POST'])
def admin_alta():
    if request.method == 'GET':
        cdx={
            "tipo":"alta",
            "admin":Admin.query.filter_by(id=id).first()
        }

        return render_template('admin/ABC_Admin.html',cdx=cdx)
    elif request.method == 'POST':
        username = request.form.get('Username')
        password = request.form.get('Password')

        e = Admin(
            username=username,
            password=password
        )
        db.session.add(e)
        db.session.commit()
        return redirect('/admin/')
        return "POST"
    else:
        return "ERROR"

@bp_admin.route('/admin/borrar/<int:id>',methods=['GET','POST'])
def borrar(id):
    if request.method == 'GET':
        cdx={
            "tipo":"borrar",
            "admin":Admin.query.filter_by(id=id).first()
        }
        return render_template('admin/ABC_Admin.html',cdx=cdx)

    elif request.method == 'POST':
        e = Admin.query.filter_by(id=id).first()
        db.session.delete(e)
        db.session.commit()
        return redirect('/admin/')
    else:
        return "ERROR"

@bp_admin.route('/admin/editar/<int:id>',methods=['GET','POST'])
def editar(id):
    if request.method == 'GET':
        cdx={
            "tipo":"editar",
            "admin":Admin.query.filter_by(id=id).first()
        }

        return render_template('admin/ABC_Admin.html',cdx=cdx)

    elif request.method == 'POST':
        username = request.form.get('Username')
        password = request.form.get('Password')
        e=Admin.query.filter_by(id=id).first()
        e.username = username
        e.password = password
        db.session.add(e)
        db.session.commit()
        return redirect("/admin/")

    else:
        return "ERROR"

@bp_admin.route('/admin/login', methods=['GET', 'POST'])
def login():
    cdx = {
        "admin": Admin.query.all()
    }
    if request.method == 'POST':
        username = request.form['Username']
        password = request.form['Password']

        # Buscar el usuario en la base de datos
        admin = Admin.query.filter_by(username=username).first()

        if admin is not None and admin.password == password:
            # Autenticación exitosa
            session['username'] = username  # Guardar el nombre de usuario en la sesión
            return render_template('/index.html', cdx=cdx)
        else:
            flash('Nombre de usuario o contraseña incorrectos')
            return render_template('admin/login.html')

@bp_admin.route('/admin/admin_login')
def admin_login():

    return render_template('admin/login.html')


@bp_admin.route('/admin/logout')
def logout():
    # Eliminar el nombre de usuario de la sesión
    session.pop('username', None)
    return render_template('admin/login.html')

@bp_admin.teardown_request
def clear_session(exception=None):
    session.pop('nombre', None)