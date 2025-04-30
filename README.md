# API de Produtos com FastAPI

Este é um projeto de uma API RESTful para gerenciamento de produtos (CRUD) construída com **FastAPI** em Python. A API permite criar, listar, atualizar e deletar produtos, utilizando um ambiente virtual gerenciado pelo **Poetry**.

## Estrutura do Projeto

Abaixo está a estrutura de diretórios do projeto:

```
api_project/
├── src/
│   ├── __init__.py
│   ├── main.py              # Arquivo principal da aplicação FastAPI
│   ├── models/
│   │   ├── __init__.py
│   │   ├── product.py       # Modelo Pydantic para produtos
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── product.py       # Rotas da API para operações CRUD
│   ├── database/
│   │   ├── __init__.py
│   │   ├── database.py      # Configuração do banco de dados (ex.: SQLite)
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── product.py       # Esquemas Pydantic para validação
├── docs/
│   ├── openapi.json         # Arquivo de especificação OpenAPI
├── tests/
│   ├── __init__.py
│   ├── test_product.py      # Testes unitários para as rotas
├── pyproject.toml           # Arquivo de configuração do Poetry
├── README.md                # Este arquivo
└── .gitignore               # Arquivo para ignorar arquivos no Git
```

## Bibliotecas Utilizadas

O projeto utiliza as seguintes bibliotecas Python:

- **fastapi**: Framework para construção da API RESTful.
- **uvicorn**: Servidor ASGI para rodar a aplicação FastAPI.
- **python-dotenv**: Gerenciamento de variáveis de ambiente.
- **sqlalchemy**: ORM para interação com o banco de dados.
- **pytest**: Framework para execução de testes unitários.
- **black**: Formatador automático de código Python.
- **flake8**: Ferramenta de linting para verificação de estilo e erros.
- **isort**: Organizador automático de imports.
- **httpx**: Cliente HTTP assíncrono para testes da API.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python** (>= 3.8)
- **Poetry** (gerenciador de dependências)
- **Git** (para clonar o repositório)

## Como Instalar e Executar

Siga os passos abaixo para clonar, configurar e executar o projeto:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/ErikSVieira/api_project.git
   cd api_project
   ```

2. **Instale o Poetry** (se ainda não estiver instalado):
   ```bash
   pip install poetry
   ```

3. **Instale as dependências do projeto**:
   ```bash
   poetry install
   ```

4. **Ative o ambiente virtual**:
   ```bash
   poetry shell
   ```

5. **Execute a aplicação**:
   ```bash
   uvicorn src.main:app --reload
   ```

   - A API estará disponível em `http://127.0.0.1:8000`.
   - Acesse a documentação interativa em `http://127.0.0.1:8000/docs`.

## Uso da API

A API possui os seguintes endpoints principais:

- **GET** `/products/` - Lista todos os produtos.
- **GET** `/products/{id}` - Retorna um produto específico.
- **POST** `/products/` - Cria um novo produto.
- **PUT** `/products/{id}` - Atualiza um produto existente.
- **DELETE** `/products/{id}` - Deleta um produto.

Consulte a documentação interativa em `/docs` ou o arquivo `docs/openapi.json` para detalhes sobre os esquemas e exemplos de requisições.

## Executando Testes

Para rodar os testes unitários, utilize:

```bash
pytest tests/
```

Certifique-se de estar no ambiente virtual do Poetry.

## Contribuindo

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. Envie para o repositório remoto (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).