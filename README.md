

# API de Usuários com Flask

Uma API RESTful para gerenciamento de usuários construída com Flask, Flask-RESTful e SQLAlchemy.
   
   ![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
   ![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)
   
## 📋 Requisitos

- Python 3.8+
- Flask 2.0+
- Flask-RESTful
- Flask-SQLAlchemy

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/samuelluzsantana/Python-REST-API.git
cd Python-REST-API
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.\.venv\Scripts\activate   # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## ⚙️ Configuração

Crie um arquivo `.env` na raiz do projeto:
```ini
FLASK_APP=api.py
FLASK_ENV=development
```

## 🏃 Executando o Projeto

```bash
python api.py
```

O servidor estará disponível em: http://localhost:5000

## 📚 Endpoints da API

### 👥 Usuários

- `GET /api/users` - Lista todos os usuários
- `POST /api/users` - Cria um novo usuário
- `GET /api/users/<id>` - Obtém um usuário específico
- `PATCH /api/users/<id>` - Atualiza um usuário
- `DELETE /api/users/<id>` - Remove um usuário

### Exemplo de Request (POST)
```json
{
  "username": "novousuario",
  "email": "novo@email.com"
}
```

## 🛠️ Estrutura do Projeto

```
.
├── api.py                # Aplicação principal
├── db.database.db        # Banco de dados SQLite (gerado automaticamente)
├── requirements.txt      # Dependências do projeto
└── README.md             # Este arquivo
```

## 🧪 Testando a API

Você pode testar a API usando:

1. **cURL**:
```bash
# Criar usuário
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"username":"teste","email":"teste@exemplo.com"}'

# Listar usuários
curl http://localhost:5000/api/users
```

2. **Postman** ou **Insomnia**


---

✨ **Dica**: Para desenvolvimento, ative o modo debug (`FLASK_ENV=development`) para ter recarregamento automático de código.
``

### Recursos adicionais que você pode incluir:


 
2. **Seção de Features**:

   ## ✨ Features
   - CRUD completo de usuários
   - Validação de dados
   - Serialização automática
   - Banco de dados SQLite


3. **Exemplo de response**:

   ### Exemplo de Response (GET /api/users/1)
   ```json
   {
     "id": 1,
     "username": "teste",
     "email": "teste@exemplo.com"
   }
   ```
