from flask import Blueprint,render_template,redirect,request
from icebreaker2.modulos.calendario.model.calendario import Calendario
from icebreaker2.modulos import db


bp_calendario = Blueprint('calendario', __name__)
print(Calendario)


@bp_calendario.route('/calendario/')
def calendario():
    cdx={
        "calendario":Calendario.query.all()
    }
    return render_template('calendario/calendario.html',cdx=cdx)

@bp_calendario.route('/calendario/alta',methods=['GET','POST'])
def calendario_alta():
    if request.method == 'POST':
        cdx={
            "tipo":"alta",
            "calendario":Calendario.query.filter_by(id=id).first()
        }
        return render_template('calendario/calendario.html',cdx=cdx)

    elif request.method == 'GET':
        nombre_cliente= request.form.get('nombre')
        apellido_cliente = request.form.get('apellido')
        fecha = request.form.get('fecha')
        monto = float(request.form.get('monto'))
        celular = request.form.get('celular')
        e = Calendario(
            nombre=nombre_cliente,
            apellido=apellido_cliente,
            fecha=fecha,
            monto=monto,
            celular=celular

        )
        db.session.add(e)
        db.session.commit()
        return redirect('/calendario/')
        return "POST"
    else:
        return "ERROR"

