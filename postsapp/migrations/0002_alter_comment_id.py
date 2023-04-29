# Generated by Django 4.2 on 2023-04-29 10:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("postsapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, primary_key=True, serialize=False
            ),
        ),
    ]
