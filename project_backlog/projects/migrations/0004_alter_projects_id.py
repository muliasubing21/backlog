# Generated by Django 4.2.18 on 2025-02-08 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_projects_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
