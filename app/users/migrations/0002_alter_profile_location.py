# Generated by Django 4.1.6 on 2023-02-11 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="location",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_location_list",
                to="users.location",
            ),
        ),
    ]