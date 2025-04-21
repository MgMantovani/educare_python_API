
# 📚 Projeto Flask - Gerenciamento de Alunos

Este é um projeto simples de CRUD (Create, Read, Update, Delete) de alunos utilizando:

- ✅ Flask (Python)
- ✅ SQLAlchemy (ORM com SQLite)
- ✅ Marshmallow (validação de dados)
- ✅ Frontend em HTML + JavaScript
- ✅ Live Server para rodar a interface no navegador

---

## 🚀 Objetivo

Permitir o cadastro, visualização, atualização e exclusão de alunos de forma simples, através de uma API REST em Flask integrada com um front-end interativo.

---

## 🛠️ Requisitos

- Python 3.8 ou superior
- Git instalado (opcional)
- Visual Studio Code (recomendado)
- Extensão [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

---

## 📦 Instalação do Projeto

### 1. Clone o projeto

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd educare_python_simplificado
```

Ou baixe o `.zip` do repositório e extraia os arquivos.

### 2. Crie o ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

- **Windows:**
  ```bash
  venv\\Scripts\\activate
  ```
- **Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

Se for utilizar o front-end no navegador, instale também o CORS:

```bash
pip install Flask-CORS
```

---

## ▶️ Executar a API Flask

No terminal (com ambiente virtual ativado), rode:

```bash
python app.py
```

A API estará disponível em:

```
http://127.0.0.1:5000
```

---

## 🌐 Executar o Frontend com Live Server

1. Abra a pasta do projeto no Visual Studio Code  
2. Clique com o botão direito no arquivo `frontend_alunos_completo.html`  
3. Escolha **"Open with Live Server"**  
Ou clique no botão **"Go Live"** no canto inferior direito do VS Code

A página abrirá em:

```
http://127.0.0.1:5500/frontend_alunos_completo.html
```

Agora você pode:

- Cadastrar alunos
- Editar alunos
- Excluir alunos
- Atualizar a lista em tempo real

---

## 🧪 Teste da API (opcional)

Você também pode testar a API com `curl`:

```bash
curl http://127.0.0.1:5000/alunos
```

---

## 🧾 Estrutura do Projeto

```
educare_python_simplificado/
├── app.py                        # API Flask
├── models.py                     # Modelos com SQLAlchemy
├── schema.py                     # Schemas com Marshmallow
├── requirements.txt              # Dependências do projeto
├── frontend_alunos_completo.html# Interface web
└── README.md                     # Documentação do projeto
```

---

## 📄 Licença

Este projeto é livre para fins educacionais.

---

## ✨ Autor

Projeto criado por **Maria Gabriela Trivelato Mantovani da Silva** como exemplo de aplicação Flask com CRUD + front-end HTML simples.
