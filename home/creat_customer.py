import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project1.settings")
django.setup()

from home.models import Customer

Customer.objects.create(name='Alfreds Futterkiste', country='Germany')
Customer.objects.create(name='Ana Trujillo Emparedados y helados', country='Mexico')
Customer.objects.create(name='Antonio Moreno Taquería', country='Mexico')
Customer.objects.create(name='Around the Horn', country='UK')
Customer.objects.create(name='Berglunds snabbköp', country='Sweden')
Customer.objects.create(name='Blauer See Delikatessen', country='Germany')
Customer.objects.create(name='Blondel père et fils', country='France')
Customer.objects.create(name='Bólido Comidas preparadas', country='Spain')
Customer.objects.create(name='Bon app', country='France')
Customer.objects.create(name='Bottom-Dollar Marketse', country='Canada')
Customer.objects.create(name='Bs Beverages', country='UK')
Customer.objects.create(name='Cactus Comidas para llevar', country='Argentina')
Customer.objects.create(name='Centro comercial Moctezuma', country='Mexico')
Customer.objects.create(name='Chop-suey Chinese', country='Switzerland')
Customer.objects.create(name='Comércio Mineiro', country='Brazil')
Customer.objects.create(name='Consolidated Holdings', country='UK')
Customer.objects.create(name='Drachenblut Delikatessend', country='Germany')
Customer.objects.create(name='Du monde entier', country='France')
Customer.objects.create(name='Eastern Connection', country='UK')