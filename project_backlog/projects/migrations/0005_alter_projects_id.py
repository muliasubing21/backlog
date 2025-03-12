# Generated by Django 4.2.18 on 2025-02-08 14:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_projects_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
