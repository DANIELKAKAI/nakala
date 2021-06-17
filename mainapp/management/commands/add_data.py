from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Product
import csv
from datetime import datetime


def format_value(value):
    try:
        return float(value.replace('KES', ''))
    except ValueError:
        return 0.00


class Command(BaseCommand):
    help = 'Populates csv data to database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs='+', type=str)

    def handle(self, *args, **options):
        for path in options['file_path']:
            with open(path) as f:
                r = list(csv.reader(f))
                for row in r[1:]:
                    _, _ = Product.objects.get_or_create(objectid=row[-1], product_variety=row[0],
                                                         commodity_type=row[1], unit=row[2], volume_in_kgs=row[3],
                                                         values_in_ksh=format_value(row[4]),
                                                         date=datetime.strptime(row[5], '%m/%d/%Y %H:%M'))
