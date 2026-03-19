# 🏘️ Comunidade API — Backend Flask

API RESTful de uma plataforma de comunidade, com autenticação de usuários,
gerenciamento de perfis e publicação de posts.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED?logo=docker)
![CI](https://github.com/TatyDePaula/comunidade-api/actions/workflows/ci.yml/badge.svg)

## ✨ Funcionalidades

- Cadastro e autenticação de usuários com Flask-Login e bcrypt
- Perfil com foto, endereço com preenchimento automático via CEP
- CRUD completo de Posts vinculados ao autor
- Validação de email único no cadastro
- Containerização com Docker
- Testes automatizados com pytest

## 🧱 Stack

- **Python 3.12** · **Flask** · **SQLAlchemy** · **Flask-Login**
- **Flask-Bcrypt** · **Flask-CORS** · **Flask-RESTX**
- **SQLite** · **Docker** · **pytest**

## 📂 Estrutura
```
comunidade-api/
├── backend/
│   ├── __init__.py        # App factory, db, login_manager
│   ├── models.py          # Modelos Usuario e Post
│   ├── usuario_routes.py  # Rotas de usuário
│   └── post_routes.py     # Rotas de post
├── tests/
│   ├── __init__.py
│   └── test_api.py        # Testes automatizados
├── instance/
│   └── comunidade.db      # Banco SQLite (gerado automaticamente)
├── .github/
│   └── workflows/
│       └── ci.yml         # GitHub Actions CI
├── main.py
├── Dockerfile
├── requirements.txt
└── .gitignore
```

## 🚀 Como rodar

### Pré-requisitos
- Docker **ou** Python 3.12+

### Com Docker (recomendado)
```bash
# Clone o repositório
git clone https://github.com/TatyDePaula/comunidade-api.git
cd comunidade-api

# Build e execução
docker build -t comunidade-api .
docker run -d -p 5000:5000 --name comunidade-api comunidade-api
```

### Localmente
```bash
git clone https://github.com/TatyDePaula/comunidade-api.git
cd comunidade-api

python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt

python main.py
```

A aplicação estará disponível em `http://127.0.0.1:5000`

## 📡 Endpoints

### Usuários
| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/api/usuarios` | Lista todos os usuários |
| GET | `/api/usuarios/<id>` | Busca usuário por ID |
| POST | `/api/usuarios` | Cria novo usuário |
| PUT | `/api/usuarios/<id>` | Atualiza usuário |
| DELETE | `/api/usuarios/<id>` | Remove usuário |

### Posts
| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/api/posts` | Lista todos os posts |
| GET | `/api/posts/<id>` | Busca post por ID |
| POST | `/api/posts` | Cria novo post |
| PUT | `/api/posts/<id>` | Atualiza post |
| DELETE | `/api/posts/<id>` | Remove post |

### Exemplo de payload — criar usuário
```json
{
  "username": "tatiane",
  "email": "taty@email.com",
  "senha": "senha123",
  "cep": "01310-100",
  "endereco": "Av. Paulista, 1000",
  "cursos": "Python, Flask"
}
```

## 🧪 Testes
```bash
pip install pytest pytest-cov
pytest tests/ -v
```

## 🐳 Monitorar logs Docker
```bash
docker logs -f comunidade-api
```

## ⚠️ Observação

Projeto configurado para desenvolvimento. Para produção,
recomenda-se usar **Gunicorn** como servidor WSGI e banco
de dados mais robusto como PostgreSQL.

## 👩‍💻 Autora

**Tatiane de Paula** — Dev Full Stack Python · AWS Cloud Practitioner  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Tatiane-blue?logo=linkedin)](https://linkedin.com/in/seu-perfil)
[![GitHub](https://img.shields.io/badge/GitHub-TatyDePaula-black?logo=github)](https://github.com/TatyDePaula)
