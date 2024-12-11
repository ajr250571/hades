# py manage.py shell < seed.py
from django.db import connection
from config.wsgi import *

# from core.erp.models import Type, Employee

# Employee delete all
# Employee.objects.all().delete()

# Type delete all and reset auto increment
# Type.objects.all().delete()
# with connection.cursor() as cursor:
#     cursor.execute(f"alter table {Type._meta.db_table} auto_increment = 1")

# Type create
# Type.objects.create(name='Efectivo')
# Type.objects.create(name='Contratado')
# Type.objects.create(name='Agencia')

# for empleado in Employee.objects.filter(type_id=1):
#     print(empleado.names)
#     print(empleado.type.name)


# for tipo in Type.objects.filter(name__icontains='Agen'):
#     print(tipo.name)
