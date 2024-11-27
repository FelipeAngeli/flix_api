
# Flix API

Flix API é um projeto desenvolvido com Django que fornece uma API para gerenciar informações sobre filmes, gêneros, atores e avaliações. O objetivo deste projeto é oferecer um backend robusto e funcional para um sistema de gerenciamento de filmes.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

- **manage.py**: Script para gerenciar comandos administrativos do Django.
- **db.sqlite3**: Banco de dados SQLite contendo os dados do sistema.
- **app**: Diretório principal do projeto.
- **genres**, **movies**, **actors**, **authentication**, **reviews**: Aplicações Django individuais para gerenciar diferentes aspectos do sistema.
- **requirements.txt** e **requirements_dev.txt**: Arquivos para gerenciar dependências do ambiente de produção e desenvolvimento.
- **movies.csv** e **actors.csv**: Dados de exemplo para importação.

## Configuração do Ambiente

### Pré-requisitos

Certifique-se de ter instalado:

- Python 3.8 ou superior
- Virtualenv
- Git

### Configuração do Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/FelipeAngeli/flix_api.git
   cd flix_api
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados e aplique as migrações:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Popule o banco de dados com os arquivos CSV, se necessário:
   ```bash
   python manage.py loaddata actors.csv movies.csv
   ```

6. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

O servidor estará disponível em `http://127.0.0.1:8000/`.

## Endpoints da API

A API oferece os seguintes recursos:

- **Filmes**:
  - Listar, criar, atualizar e deletar filmes.
- **Gêneros**:
  - Listar gêneros disponíveis.
- **Atores**:
  - Listar e gerenciar informações de atores.
- **Autenticação**:
  - Gerenciamento de usuários e autenticação via JWT.
- **Avaliações**:
  - Criar e listar avaliações para filmes.

### Exemplo de Requisição

#### Listar Filmes

`GET /api/movies/`

Resposta:
```json
[
  {
    "id": 1,
    "title": "O Poderoso Chefão",
    "genre": "Crime",
    "release_date": "1972-03-14",
    "actors": ["Marlon Brando", "Al Pacino"]
  }
]
```

## Testes

Para executar os testes do projeto:

1. Instale as dependências de desenvolvimento:
   ```bash
   pip install -r requirements_dev.txt
   ```

2. Execute os testes:
   ```bash
   python manage.py test
   ```

## Contribuição

Contribuições são bem-vindas! Siga estas etapas:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça commit das suas alterações.
4. Envie um pull request.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
