from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Aluno(db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    idade = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "email": self.email, "idade": self.idade}
