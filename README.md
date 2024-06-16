# Boas-vindas ao repositório do Exercício: Flask - Student Service

<summary>🧑‍💻 O que deverá ser desenvolvido</summary>

- Nesse exercício você irá construir um modelo que representará estudantes. Além disso, você vai precisar construir os endpoints para criar, ler, resgatar, atualizar e deletar estudantes do nosso banco de dados MongoDB.

</details>

<details>
  <summary>📝 Habilidades a serem trabalhadas </summary>

Neste projeto, verificamos se você é capaz de:

- Implementar uma API utilizando arquitetura em camadas MVC.
- Aplicar conhecimentos de Orientação a Objetos no desenvolvimento WEB.
- Escrever testes para APIs para garantir a implementação dos endpoints.
- Interagir com um banco de dados não relacional MongoDB.

</details>

## Preparando Ambiente

<details>

<summary>🐳 Subindo a aplicação</summary>

**[1]** Crie o ambiente virtual para o projeto

```bash
python3 -m venv .venv && source .venv/bin/activate
```

**[2]** Instale as dependências

```bash
python3 -m pip install -r dev-requirements.txt
```

**Escolha uma opção:**

- Lembre de sua escolha para rodar as Seeds depois do Req.1

**[3 - Opção A]** Banco e Flask pelo Docker

```bash
docker compose up
```

- Recomendada: Dockerfile e Docker-compose já estão prontos para uso, para conectar o MongoDB e o Flask.

**[3 - Opção B]** Banco pelo Docker, Flask localmente pelo ambiente virtual

```bash
docker compose up -d mongodb

python3 src/app.py
```

**[4]** O projeto utilizará a Pymongo, mas se preocupe pouco com o Mongodb, pois assim como no conteúdo, você precisará penas herdar a classe abstrata [abstract_model](src/model/abstract_model.py) em sua model, para que tenha acesso aos principais métodos de manipulação do banco.

</details>

----

## Requisitos

### 1 - Implemente o atributo `_collection` em `StudentModel`

local:`src/models/student_model.py`

Antes de começar a desenvolver, vale a pena inspecionar os arquivos `src/database/db.py` e `src/models/abstract_model.py` que contém, respectivamente, a lógica para conexão com o banco de dados e o modelo que abstrai toda as interações com o MongoDB.

Você deverá:

- fazer com que a model `StudentModel` use a coleção `students` através da definição do atributo protegido `collection`;


<details>
<summary>O que será testado:</summary>

- Se o atributo protegido `_collections`, na model `StudentModel`, foi definido corretamente com o valor `students`;
- 
</details>

### 2 - Implemente o método `to_dict` e o método inicializador em `StudentModel`

local:`src/models/student_model.py`

Você deverá:

- Implementar corretamente o método `to_dict`. Ele deve retornar um dicionário contendo os atributos `name` e `enrollment_number` da instância. O atributo `name` representa o nome da pessoa estudante registrada e o atributo `enrollment_number` representa o dessa mesma pessoa.
- Definir corretamente o método inicializador `__init__`, recebendo um parâmetro e fazendo com que ele use a lógica de inicialização da classe herdada.

### 3 - Implemente a rota `/students` para listar estudantes

local:`src/controllers/student_controller.py`

A partir de agora serão implementados alguns _endpoints_ e você já poderá visualizar o resultado no navegador e/ou _thunderclient_. Execute um dos comandos a seguir para popular o banco com alguns estudantes:

```bash
# Opção A. Caso esteja usando o Flask e o banco pelo Docker:
docker compose exec -it student python3 src/seed.py

# Opção B. Caso esteja usando apenas o banco pelo Docker:
python3 src/seed.py
```

Você deverá:

- Criar o arquivo da controller que utilizará para implementar as rotas.
- Implementar a operação _HTTP_ `GET` na rota `/students` que retorna uma lista de dicionários com os dados de todos os estudantes cadastrados no banco de dados.
- A resposta deve retornar o status `200` e caso não sejam encontrados dados no banco, deve retornar uma lista vazia.

### 4 - Implemente a rota `/students/<enrollment>` para exibir dados de uma pessoa estudante

local:`src/controllers/student_controller.py`

Você deverá:

- Implementar a operação _HTTP_ `GET` na rota `/students/<enrollment>` que retorna um dicionário com os dados da pessoa estudante que possua `<enrollment>` como número de matrícula.
- Em caso de sucesso, a resposta deve retornar o status `200`.
- Caso não seja encontrado um estudante com o número de matrícula informado, a resposta deve retornar o status `404` e nenhum conteúdo no corpo da requisição.

### 5 - Implemente a rota `/students` para criar uma pessoa estudante

local:`src/controllers/student_controller.py`

Você deverá:

- Implementar a operação _HTTP_ `POST` na rota `/students`. O método deve inserir corretamente a pessoa estudante no banco e retornar um dicionário com dessa mesma pessoa estudante.
- Em caso de sucesso, a resposta deve retornar o status `201`.
- Caso uma das chaves (`name` ou `enrollment_number`) esteja faltando no corpo da requisição, deve-se retornar o status code `400`.
  
### 6 - Implemente a rota `/students/<enrollment>` para deletar uma pessoa estudante

local:`src/controllers/student_controller.py`

Você deverá:

- Implementar a operação _HTTP_ `DELETE` na rota `/students/<enrollment>`. O método deve remover corretamente a pessoa estudante cuja matrícula seja `<enrollment>` do banco.
- Em caso de sucesso, a resposta deve retornar o status `204` e nenhum conteúdo.
- Em caso de não se encontrar uma pessoa estudante com o número de matrícula informado, a resposta deve retornar o status `404` e nenhum conteúdo no corpo da requisição.
  
### 7 - Sobrescreva o método `update` em `StudentModel`

local:`src/models/student_model.py`

Você deverá:

- Sobrescrever corretamente o método `update`. O método `update`, originalmente, usa o `_id` para buscar um registro dentro da coleção, contudo, para o caso deste exercício, queremos utilizar o número único de matrícula para fazer esse resgate.
- O novo método `update` deve usar a chave `enrollment_number` para buscar um registro dentro da coleção e atualizar os dados da pessoa estudante.
- O novo método `update` deve retornar um dicionário com os dados da pessoa estudante atualizados.

### 8 - Implemente a rota `/students/<enrollment>` para atualizar os dados de uma pessoa estudante

local:`src/controllers/student_controller.py`

Você deverá:

- Implementar a operação _HTTP_ `PUT` na rota `/students/<enrollment>`. O método deve atualizar corretamente os dados da pessoa estudante cuja matrícula seja `<enrollment>` no banco.
- Em caso de sucesso, a resposta deve retornar o status `200` e um dicionário já com os dados atualizados.
- Em caso de não se encontrar uma pessoa estudante com o número de matrícula informado, a resposta deve retornar o status `404` e nenhum conteúdo no corpo da requisição.
  
----
