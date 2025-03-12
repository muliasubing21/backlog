# Generated by Django 4.2.18 on 2025-03-05 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_tasks_assigned_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('TODO', 'To Do'), ('IN_PROGRESS', 'In Progress'), ('DONE', 'Done')], default='TODO', max_length=20),
        ),
    ]
