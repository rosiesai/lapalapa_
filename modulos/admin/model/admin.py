from icebreaker2.modulos import db


class Admin(db.Model):
    __tablename__='Administradores'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))


    def __int__(self,id,username,password):
        self.id = id
        self.username = username
        self.password = password


    def __repr__(self):
        return f"({self.id}) {self.username} {self.password} "