from django.core.management.base import BaseCommand

from ...models import Tag

# Tag.objects.all().delete()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(f"static/docs/tag_list.txt") as file:
            for row in file:
                tag = row.replace("\n", "")
                Tag.objects.get_or_create(
                    tag=tag,
                )
                self.stdout.write(self.style.SUCCESS(f"{tag} added"))
        self.stdout.write(self.style.SUCCESS("list of tags added"))
