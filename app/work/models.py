from django.conf import settings
from django.db import models
from users.models import Location
from django.urls import reverse

Seller = settings.AUTH_USER_MODEL


class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.tag}"


class SkillLevel(models.Model):
    skill_level = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.skill_level}"


class Work(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    posted_by = models.ForeignKey(Seller, on_delete=models.CASCADE)
    skill_level = models.ForeignKey(SkillLevel, on_delete=models.SET_DEFAULT, default=2)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True, blank=True
    )
    postal_code = models.CharField(
        max_length=8, help_text="eg: LC03 101", null=True, blank=True
    )
    tags = models.ManyToManyField(Tag)
    # likes = models.BooleanField(default=False)
    # dislikes = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("work-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
