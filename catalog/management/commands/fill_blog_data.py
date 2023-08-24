import json
from django.core.management import BaseCommand
from catalog.models import Blog


class Command(BaseCommand):

    @staticmethod
    def delete_everything():
        Blog.objects.all().delete()

    def handle(self, *args, **options):
        self.delete_everything()

        with open('blog_dumpdata.json', 'r', encoding='utf-8') as json_file:
            loaded_blogs = [Blog(pk=data.get('pk'), **data['fields']) for data in json.load(json_file)]

        Blog.objects.bulk_create(loaded_blogs)
