import csv, sys, os

project_dir = "/Users/konstantingolubtsov/Desktop/Personal/Development education/CS50 Web/project3/project3/pizza"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from menu.models import product

data = csv.reader(open("/Users/konstantingolubtsov/Desktop/Personal/Development education/CS50 Web/project3/project3/menu.csv"),delimiter = ',')
for row in data:
    item = product()
    item.category = row[0]
    item.name = row[1]
    item.small_price = row[2]
    item.large_price = row[3]
    item.save()
