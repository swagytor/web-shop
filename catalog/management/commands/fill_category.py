import json
from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    @staticmethod
    def delete_everything():
        Category.objects.all().delete()

    def handle(self, *args, **options):
        self.delete_everything()

        with open('category_dumpdata.json', 'r', encoding='utf-8') as json_file:
            loaded_data = [Category(pk=data.get('pk'), **data['fields']) for data in json.load(json_file)]

        Category.objects.bulk_create(loaded_data)
