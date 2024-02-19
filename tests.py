from config.wsgi import *

from core.erp.models import Type

# query = Type.objects.all()
# print(query)


# Agregar
try:
    t = Type()
    t.name = "Portero"
    t.save()
except Exception as e:
    print(e)

# Modificar
# try:
#    t = Type.objects.get(id=1)
#    t.name = "Electricista"
#    t.save()
# except Exception as e:
#    print(e)

for i in Type.objects.filter(name__endswith="o").exclude(id=3)[:2]:
    print(i.name)

# q = Type.objects.all()
# print(q)
