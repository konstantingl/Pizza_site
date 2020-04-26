import csv, sys, os

project_dir = "/Users/konstantingolubtsov/Desktop/Personal/Development education/CS50 Web/project3/project3/pizza"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from menu.models import topping

data = csv.reader(open("/Users/konstantingolubtsov/Desktop/Personal/Development education/CS50 Web/project3/project3/w_items/topings.csv"),delimiter = ',')
for row in data:
    item = topping()
    item.topping_name = row[0]
    item.save()
