import csv, sys, os

project_dir = "/Users/konstantingolubtsov/Desktop/Personal/Development education/CS50 Web/project3/project3/pizza"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from orders.models import toppings

data = csv.reader(open("/Users/konstantingolubtsov/Desktop/Personal/Development education/CS50 Web/project3/project3/menu.csv"),delimiter = ',')
for row in data:
    item = toppings()
    item.topping_name = row[0]
    item.save()
