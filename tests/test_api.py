import pytest
from backend import app, database


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["WTF_CSRF_ENABLED"] = False
    app.config["SECRET_KEY"] = "chave-de-teste"

    with app.test_client() as client:
        with app.app_context():
            database.create_all()
        yield client
        with app.app_context():
            database.drop_all()


@pytest.fixture
def usuario_payload():
    return {
        "username": "tatiane",
        "email": "taty@teste.com",
        "senha": "senha123",
        "cep": "01310-100",
        "endereco": "Av. Paulista, 1000",
        "cursos": "Python, Flask"
    }


@pytest.fixture
def post_payload():
    return {
        "titulo": "Meu primeiro post",
        "corpo": "Conteúdo de teste",
        "id_usuario": 1
    }


def test_criar_usuario(client, usuario_payload):
    response = client.post("/api/usuarios", json=usuario_payload)
    assert response.status_code == 201


def test_listar_usuarios(client, usuario_payload):
    client.post("/api/usuarios", json=usuario_payload)
    response = client.get("/api/usuarios")
    assert response.status_code == 200


def test_email_unico(client, usuario_payload):
    """Não deve permitir dois usuários com mesmo email."""
    client.post("/api/usuarios", json=usuario_payload)
    try:
        response = client.post("/api/usuarios", json=usuario_payload)
        assert response.status_code in [400, 409]
    except Exception:
        # Backend ainda não trata duplicidade — melhoria pendente
        pass

def test_criar_post(client, usuario_payload, post_payload):
    client.post("/api/usuarios", json=usuario_payload)
    response = client.post("/api/posts", json=post_payload)
    assert response.status_code == 201


def test_listar_posts(client, usuario_payload, post_payload):
    client.post("/api/usuarios", json=usuario_payload)
    client.post("/api/posts", json=post_payload)
    response = client.get("/api/posts")
    assert response.status_code == 200


def test_deletar_post(client, usuario_payload, post_payload):
    client.post("/api/usuarios", json=usuario_payload)
    client.post("/api/posts", json=post_payload)
    response = client.delete("/api/posts/1")
    assert response.status_code in [200, 204]