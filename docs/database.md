# Banco de Dados
O Banco de dados utilizado é um PostgreSQL. Neste documento é apresentado como gerenciar o banco de dados pelas ferramentas Alembic e SQLAlchemy 

## Migrations
As Migrations são gerenciadas pela ferramenta Alembic e estão localizadas em ```/bd/versions```.

### Como Rodar as Migrations?

1. Para rodar todas
```
alembic upgrade head
```

2. Para rodar apenas 1 quantidade
```
alembic upgrade +1
```

### Como Gerar uma nova Migration
O Alembic está integrado com o SQLAlchemy. Para isso é necessário criar um novo modelo ou modificar um já existente.

1. Importe o modelo no arquivo ```/bd/models.py```, caso não esteje lá.
2. Utilize o comando ```alembic revision --autogenerate -m "comentário"
3. Análise a migration criada
4. Execute ```alembic upgrade head``` para rodar a migration, caso esteja correta.