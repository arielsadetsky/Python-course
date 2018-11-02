from sqlalchemy import select
from core import user_table
from pprint import pprint

result = select([user_table])
result2 = select([user_table]).where(user_table.c.nome == 'daniel')

registros = []
for registro in result.execute():
    registros.append(registro)
pprint(registros)