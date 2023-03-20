import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from PIL import Image


class User(AbstractUser):
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


class Location(models.Model):
    location_name = models.CharField(max_length=100)

    class Meta:
        ordering = ("location_name",)

    def __str__(self):
        return self.location_name.title()


class Title(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name.title()


class Profile(models.Model):
    GENDER_LIST = [
        ("F", "F"),
        ("M", "M"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name="user_title_list",
        null=True,
        blank=True,
    )
    image = models.ImageField(blank=True, null=True, upload_to="profile_photos")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, blank=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_LIST, default=GENDER_LIST[0][0]
    )
    address = models.CharField(max_length=255, blank=True)
    address1 = models.CharField(max_length=255, blank=True)
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="user_location_list",
        null=True,
        blank=True,
    )
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    dob = models.DateField("DOB", blank=True, null=True)
    phone = models.TextField(null=True, default="+1")
    phone1 = models.TextField(blank=True)
    bio = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.uid)
        super(Profile, self).save(*args, **kwargs)

       # Open the image using Pillow
        with Image.open(self.image.path) as img:
            # Get the size of the image
            width, height = img.size

            # Find the smallest dimension
            smallest_dim = min(width, height)

            # Calculate the box to crop the image to
            left = (width - smallest_dim) / 2
            top = (height - smallest_dim) / 2
            right = (width + smallest_dim) / 2
            bottom = (height + smallest_dim) / 2

            # Crop the image
            cropped_img = img.crop((left, top, right, bottom))

            # Resize the image to 500x500 pixels
            resized_img = cropped_img.resize((500, 500))

            # Save the resized image back to the same path
            resized_img.save(self.image.path)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("profile", kwargs={"slug": self.slug})

    def get_profile_initials(self):
        return f"{self.first_name[0]} {self.last_name[0]}"

    def __str__(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.user.email
