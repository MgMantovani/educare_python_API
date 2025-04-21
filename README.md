### 📄 `README.md`

```markdown
# 📚 Projeto Flask - Gerenciamento de Alunos

Este é um projeto simples de CRUD (Create, Read, Update, Delete) de alunos utilizando:

- ✅ Flask (Python)
- ✅ SQLAlchemy (ORM com SQLite)
- ✅ Marshmallow (validação)
- ✅ Frontend em HTML + JavaScript
- ✅ Live Server para rodar a interface no navegador

---

## 🚀 Objetivo

Criar, visualizar, atualizar e excluir alunos de forma simples através de uma API Flask e um front-end HTML interativo.

---

## 🛠️ Requisitos

- Python 3.8 ou superior
- Git instalado (opcional)
- Visual Studio Code (recomendado)
- Extensão [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) no VS Code

---

## 📦 Instalação do Projeto

### 1. Clone o projeto

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd educare_python_simplificado
```

Ou baixe o `.zip` e extraia os arquivos.

---

### 2. Crie o ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

- **Windows**:
  ```bash
  venv\\Scripts\\activate
  ```

- **Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```

---

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

Se estiver usando o front-end no navegador, adicione também o CORS:

```bash
pip install Flask-CORS
```

---

## ▶️ Executar a API Flask

No terminal (com o ambiente ativado), rode:

```bash
python app.py
```

A API estará disponível em:

```
http://127.0.0.1:5000
```

---

## 🌐 Rodar o Frontend com Live Server

### 1. Abra a pasta do projeto no **Visual Studio Code**

### 2. Clique com o botão direito no arquivo `frontend_alunos_completo.html`

Escolha:

```
"Open with Live Server"
```

Ou clique no botão "Go Live" no canto inferior direito do VS Code.

### 3. O navegador abrirá uma página como:

```
http://127.0.0.1:5500/frontend_alunos_completo.html
```

### 4. Agora você pode:

- Cadastrar alunos
- Editar alunos
- Excluir alunos
- Atualizar a lista em tempo real

---

## 🧪 Teste da API (opcional)

Você também pode testar manualmente via `curl`:

```bash
curl http://127.0.0.1:5000/alunos
```

---

## 🧾 Estrutura do Projeto

```
educare_python_simplificado/
├── app.py                   # API Flask
├── models.py                # Modelo do banco de dados
├── schema.py                # Validação com Marshmallow
├── requirements.txt         # Dependências
├── frontend_alunos_completo.html  # Interface HTML
└── README.md                # Documentação
```

---

## 📄 Licença

Este projeto é livre para fins educacionais.

---

## ✨ Autor

Projeto criado por Maria Gabriela Trivelato Mantovani da Silva como exemplo de aplicação Flask com CRUD + front-end simples.


