from django.core.management.base import BaseCommand

from ...models import SkillLevel


class Command(BaseCommand):
    # def add_arguments(self, parser):
    #     parser.add_argument("file_name", type=str)

    def handle(self, *args, **kwargs):
        # file_name = kwargs["file_name"]
        with open(f"static/docs/skill_level_list.txt") as file:
            for row in file:
                skill_level = row.lower().replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{skill_level} added"))
                SkillLevel.objects.get_or_create(
                    skill_level=skill_level,
                )
        self.stdout.write(self.style.SUCCESS("list of skill levels added"))
