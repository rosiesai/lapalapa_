from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('configuration.DevelopmentConfig')
db = SQLAlchemy(app)

from icebreaker2.modulos.home.views import bp_home
from icebreaker2.modulos.productos.views import bp_prod
from icebreaker2.modulos.empleados.views import bp_emp
from icebreaker2.modulos.calendario.views import bp_calendario
from icebreaker2.modulos.admin.views import bp_admin

app.register_blueprint(bp_home)
app.register_blueprint(bp_prod)
app.register_blueprint(bp_emp)
app.register_blueprint(bp_calendario)
app.register_blueprint(bp_admin)

with app.app_context():
    db.create_all()