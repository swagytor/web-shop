import json
from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def delete_everything():
        Category.objects.all().delete()
        Product.objects.all().delete()

    def handle(self, *args, **options):
        self.delete_everything()

        with open('category_dumpdata.json', 'r', encoding='utf-8') as json_file:
            loaded_categories = [
                Category(pk=data.get('pk'), **data['fields']) for data in json.load(json_file)]

        with open('product_dumpdata.json', 'r', encoding='utf-8') as json_file:
            loaded_products = [
                Product(pk=data.get('pk'), product_category_id=data['fields']['product_category'],
                        product_name=data['fields']['product_name'],
                        product_description=data['fields']['product_description'],
                        product_image=data['fields']['product_image'], product_price=data['fields']['product_price'],
                        date_of_creation=data['fields']['date_of_creation'],
                        date_of_last_change=data['fields']['date_of_last_change']) for
                data in json.load(json_file)]

        Category.objects.bulk_create(loaded_categories)
        Product.objects.bulk_create(loaded_products)
