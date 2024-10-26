from database import db

class Basquete(db.Model):
    __tablename__='basquete'
    id_basquete = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    cidade= db.Column(db.String(50))
    numero_titulos = db.Column(db.Integer)

    def __init__(self, nome, cidade, numero_titulos):
        self.nome = nome
        self.cidade = cidade
        self.numero_titulos = numero_titulos

    def __repr__(self):
        return "<Jogadores de basquete {}>".format(self.nome)
    
        