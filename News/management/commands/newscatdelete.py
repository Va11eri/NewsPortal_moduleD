from django.core.management.base import BaseCommand
from ...models import Post, Category

class Command(BaseCommand):
    help = 'Delete all news in a chosen category'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Do you want to delete news in the category "{options["category"]}"? yes/no: ')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Canceled'))
            return

        try:
            category = Category.objects.get(name=options['category'])
            posts = Post.objects.filter(postcategory__category=category)
            posts.delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted all news from the category "{category.name}"'))
        except Category.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find the category "{options["category"]}"'))
