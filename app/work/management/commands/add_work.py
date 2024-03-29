import random

from django.conf import settings
from django.core.management.base import BaseCommand
from faker import Faker
from users.models import Location, User

from ...models import SkillLevel, Work
from users.models import Location


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(200):
            Work.objects.get_or_create(
                title=fake.company(),
                description=fake.paragraph(nb_sentences=7),
                posted_by=User.objects.get(pk=User.objects.first().pk),
                skill_level=SkillLevel.objects.get(pk=random.randint(1, 4)),
                hourly_rate=random.randint(7, 35),
                location=Location.objects.get(pk=random.randint(1, Location.objects.count())),
            )
        self.stdout.write(self.style.SUCCESS("jobs added"))
