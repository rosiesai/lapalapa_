from icebreaker2.modulos import db


class Empleado(db.Model):
    __tablename__='Clientes'
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255))
    apellido = db.Column(db.String(255))
    fecha = db.Column(db.String(255))
    monto = db.Column(db.Float)
    celular = db.Column(db.String(255))
    comentarios = db.Column(db.String(255))

    def __int__(self,id,nombre,apellido,fecha,monto,celular,comentarios=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.fecha = fecha
        self.monto = monto
        self.comentarios = comentarios
        self.celular = celular


    def __repr__(self):
        return f"({self.id}) {self.nombre} {self.apellido} {self.fecha} {self.monto} {self.comentarios}{self.celular}"