# py seed.py
from django.db import connection
from config.wsgi import *
from core.erp.models import Category

Category.objects.all().delete()
with connection.cursor() as cursor:
    cursor.execute(f"alter table {Category._meta.db_table} auto_increment = 1")

categorias = [
    "Frutas frescas",
    "Verduras frescas",
    "Carnes rojas",
    "Carnes blancas",
    "Pescados",
    "Mariscos",
    "Lácteos",
    "Quesos",
    "Yogures",
    "Huevos",
    "Pan fresco",
    "Pasteles y postres",
    "Cereales para desayuno",
    "Arroz",
    "Pasta",
    "Legumbres secas",
    "Legumbres enlatadas",
    "Conservas de vegetales",
    "Salsas",
    "Condimentos",
    "Especias",
    "Aceites",
    "Vinagres",
    "Sal y azúcar",
    "Snacks salados",
    "Snacks dulces",
    "Chocolates",
    "Dulces y caramelos",
    "Helados",
    "Congelados preparados",
    "Verduras congeladas",
    "Frutas congeladas",
    "Carnes congeladas",
    "Pizzas congeladas",
    "Bebidas alcohólicas",
    "Vinos",
    "Cervezas",
    "Licores",
    "Bebidas sin alcohol",
    "Refrescos",
    "Jugos naturales",
    "Jugos envasados",
    "Aguas minerales",
    "Café",
    "Té",
    "Infusiones",
    "Bebidas energéticas",
    "Leche de vaca",
    "Leches vegetales",
    "Alternatives a la carne",
    "Tofu",
    "Tempeh",
    "Seitan",
    "Frutos secos",
    "Semillas",
    "Mermeladas",
    "Miel",
    "Conservas de frutas",
    "Sopas enlatadas",
    "Caldos y sopas",
    "Sushi preparado",
    "Comida preparada para llevar",
    "Hamburguesas",
    "Salchichas",
    "Embutidos",
    "Jamones",
    "Pastas frescas",
    "Ingredientes para repostería",
    "Levadura",
    "Masa de hojaldre",
    "Productos dietéticos",
    "Alimentos orgánicos",
    "Alimentos sin gluten",
    "Complementos alimenticios",
    "Cereales integrales",
    "Harinas",
    "Levaduras y polvo de hornear",
    "Masas preparadas",
    "Aderezos",
    "Mostazas",
    "Kétchup",
    "Encurtidos",
    "Aceitunas",
    "Productos étnicos",
    "Comida mexicana preparada",
    "Comida china preparada",
    "Comida italiana preparada",
    "Alimentos para dietas especiales",
    "Proteínas en polvo",
    "Barras energéticas",
    "Suplementos nutricionales",
    "Bebidas proteicas",
    "Productos veganos",
    "Productos vegetarianos"
]

for categoria in categorias:
    Category.objects.create(name=categoria)

# from core.erp.models import Category

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
