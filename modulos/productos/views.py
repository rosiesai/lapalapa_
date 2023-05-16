from flask import Blueprint,render_template

bp_prod = Blueprint('productos', __name__)

@bp_prod.route('/productos')
def productos():
    return render_template('productos/productos.html')