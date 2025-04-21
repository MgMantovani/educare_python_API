from flask import Flask, request, jsonify
from models import db, Aluno
from schema import AlunoSchema
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # <- permite acesso do front-end

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.url_map.strict_slashes = False  # <- adicionado aqui


db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "API simplificada rodando!"

@app.route("/alunos", methods=["GET"])
def get_alunos():
    alunos = Aluno.query.all()
    return jsonify([a.to_dict() for a in alunos])

@app.route("/alunos", methods=["POST"])
def create_aluno():
    data = request.get_json()
    schema = AlunoSchema()
    try:
        validated = schema.load(data)
        aluno = Aluno(**validated)
        db.session.add(aluno)
        db.session.commit()
        return jsonify(aluno.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"erro": "Email já cadastrado"}), 400
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@app.route("/alunos/<int:aluno_id>", methods=["PUT"])
def update_aluno(aluno_id):
    aluno = Aluno.query.get_or_404(aluno_id)
    data = request.get_json()
    schema = AlunoSchema()
    try:
        validated = schema.load(data)
        aluno.nome = validated["nome"]
        aluno.email = validated["email"]
        aluno.idade = validated["idade"]
        db.session.commit()
        return jsonify(aluno.to_dict())
    except IntegrityError:
        db.session.rollback()
        return jsonify({"erro": "Email já cadastrado"}), 400
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@app.route("/alunos/<int:aluno_id>", methods=["DELETE"])
def delete_aluno(aluno_id):
    aluno = Aluno.query.get_or_404(aluno_id)
    try:
        db.session.delete(aluno)
        db.session.commit()
        return jsonify({"mensagem": "Aluno deletado com sucesso"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
