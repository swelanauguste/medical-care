from django.core.management.base import BaseCommand

from ...models import Title

# Tag.objects.all().delete()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(f"static/docs/title_list.txt") as file:
            for row in file:
                name = row.replace("\n", "")
                Title.objects.get_or_create(
                    name=name,
                )
                self.stdout.write(self.style.SUCCESS(f"{name} added"))
        self.stdout.write(self.style.SUCCESS("list of tags added"))
