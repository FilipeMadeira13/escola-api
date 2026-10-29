# Escola API

API REST para gerenciamento de estudantes, cursos e matrículas, desenvolvida com Django e Django REST Framework.

## Funcionalidades

- Cadastro, consulta, atualização e exclusão de estudantes, cursos e matrículas.
- Consulta dos cursos em que um estudante está matriculado.
- Consulta dos estudantes matriculados em um curso.
- Autenticação por usuário e senha.
- Administração dos registros pelo Django Admin.

## Tecnologias

- Python
- Django
- Django REST Framework
- SQLite
- python-dotenv

As versões das dependências estão definidas em `requirements.txt`.

## Execução local

### 1. Clone o repositório

```bash
git clone https://github.com/FilipeMadeira13/escola-api.git
cd escola-api
```

### 2. Prepare o ambiente

Com Python e pip instalados, crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

Linux e macOS:

```bash
source .venv/bin/activate
```

Windows — PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente

Gere uma chave para o ambiente local:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Crie um arquivo `.env` na raiz do projeto e insira a chave gerada:

```dotenv
DJANGO_SECRET_KEY='substitua-pela-chave-gerada'
```

O arquivo `.env` é ignorado pelo Git. Não compartilhe sua chave secreta.

### 4. Prepare o banco de dados

```bash
python manage.py migrate
```

O projeto utiliza SQLite. O arquivo `db.sqlite3` será criado localmente.

### 5. Crie um usuário

```bash
python manage.py createsuperuser
```

Esse usuário poderá acessar a API e o painel administrativo.

### 6. Inicie o servidor

```bash
python manage.py runserver
```

Acessos locais:

- API: http://127.0.0.1:8000/
- Administração: http://127.0.0.1:8000/admin/

## Autenticação

A API exige autenticação HTTP Basic, com usuário e senha do Django.

Exemplo de consulta com curl, que solicitará a senha:

```bash
curl --user seu_usuario http://127.0.0.1:8000/estudantes/
```

O painel administrativo utiliza o formulário de login do Django.

## Endpoints

Os caminhos abaixo são relativos à URL base da API.

| Recurso | Caminho | Métodos |
| --- | --- | --- |
| Estudantes | `/estudantes/` | GET, POST |
| Estudante por ID | `/estudantes/{id}/` | GET, PUT, PATCH, DELETE |
| Cursos | `/cursos/` | GET, POST |
| Curso por ID | `/cursos/{id}/` | GET, PUT, PATCH, DELETE |
| Matrículas | `/matriculas/` | GET, POST |
| Matrícula por ID | `/matriculas/{id}/` | GET, PUT, PATCH, DELETE |
| Matrículas de um estudante | `/estudantes/{id}/matriculas/` | GET |
| Matrículas de um curso | `/cursos/{id}/matriculas/` | GET |

`PUT` substitui os dados do recurso; `PATCH` atualiza apenas os campos enviados.

### Exemplos de dados para cadastro

Estudante — `POST /estudantes/`:

```json
{
  "nome": "Estudante de Exemplo",
  "email": "estudante@example.com",
  "cpf": "00000000000",
  "data_nascimento": "2000-01-15",
  "numero_celular": "11999999999"
}
```

Os dados acima são fictícios.

Curso — `POST /cursos/`:

```json
{
  "codigo": "PY01",
  "descricao": "Introdução ao Python",
  "nivel": "B"
}
```

Matrícula — `POST /matriculas/`:

```json
{
  "estudante": 1,
  "curso": 1,
  "periodo": "M"
}
```

Substitua os IDs pelos registros existentes no banco.

### Valores aceitos

| Campo | Código | Significado |
| --- | --- | --- |
| Nível do curso | `B` | Básico |
| Nível do curso | `I` | Intermediário |
| Nível do curso | `A` | Avançado |
| Período da matrícula | `M` | Matutino |
| Período da matrícula | `V` | Vespertino |
| Período da matrícula | `N` | Noturno |

A consulta por estudante retorna a descrição do curso e o nome do período. A consulta por curso retorna os nomes dos estudantes matriculados.

Excluir um estudante ou curso também exclui suas matrículas relacionadas.

## Estrutura do projeto

```text
escola/
├── migrations/       # Histórico de alterações do banco
├── admin.py          # Configuração do painel administrativo
├── models.py         # Estudantes, cursos e matrículas
├── serializers.py    # Conversão e validação dos dados da API
├── tests.py          # Arquivo reservado para testes
└── views.py          # Operações e consultas da API
setup/
├── settings.py       # Configurações do Django
└── urls.py           # Rotas da aplicação
manage.py             # Comandos administrativos
requirements.txt      # Dependências do projeto
```

## Verificações

Verifique a configuração do Django:

```bash
python manage.py check
```

Execute os testes disponíveis:

```bash
python manage.py test
```

Atualmente, `escola/tests.py` ainda não contém casos de teste implementados.

## Ambiente de desenvolvimento

A configuração atual utiliza `DEBUG=True`, SQLite e o servidor local do Django.

A publicação em produção exige configuração própria, incluindo `DEBUG=False`, hosts permitidos, gestão de segredos e HTTPS para proteger as credenciais utilizadas pela autenticação HTTP Basic.
