import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria.settings")

import django
django.setup()

from pizza.models import Pizza

pizzas = Pizza.objects.all()

for pizza in pizzas:
    print(pizza.id, pizza)