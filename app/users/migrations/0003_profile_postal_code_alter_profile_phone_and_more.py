# Generated by Django 4.1.6 on 2023-03-02 14:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_title_profile_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="postal_code",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="phone",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="phone1",
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
