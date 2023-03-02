import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from users.models import User


class Qualification(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class MedicalCareProfile(models.Model):
    carer = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="carer_profile"
    )
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    uid = models.UUIDField(
        default=uuid.uuid4, editable=False, blank=True, null=True, unique=True
    )
    hourly_rate = models.DecimalField(decimal_places=2, max_digits=9, default=5)
    qualifications = models.ManyToManyField(
        Qualification, related_name="qualification_list", blank=True
    )
    skills = models.ManyToManyField(Skill, related_name="skill_list", blank=True)
    exp = models.CharField(
        "experience",
        max_length=255,
        help_text="years of experience",
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.uid)
        super(MedicalCareProfile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("medical-care-profile-detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("medical-care-profile-update", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.carer.profile}"
