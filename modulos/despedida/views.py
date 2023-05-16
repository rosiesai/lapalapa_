from flask import Blueprint

bp_saybye = Blueprint('saybye',__name__)

@bp_saybye.route('/saybye/<name>/')
def saybye(name):
    return f"adios mundo cruel {name}"