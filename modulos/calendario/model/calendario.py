from icebreaker2.modulos import db


class Calendario(db.Model):
    __tablename__='Calendario'
    id = db.Column(db.Integer,primary_key=True)
    nombre_cliente = db.Column(db.String(255))
    apellido_cliente = db.Column(db.String(255))
    celular_cliente = db.Column(db.String(255))
    paquete = db.Column(db.String(255))
    fecha = db.Column(db.String(255))
    monto = db.Column(db.String(255))

    def __int__(self,nombre_cliente,apellido_cliente,celular_cliente,paquete,fecha,monto):
        self.nombre_cliente = nombre_cliente
        self.apellido_cliente = apellido_cliente
        self.celular_cliente = celular_cliente
        self.paquete = paquete
        self.fecha = fecha
        self.monto = monto


    def __repr__(self):
        return f"({self.id}) {self.nombre_cliente} {self.apellido_cliente}"