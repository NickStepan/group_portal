# Generated by Django 5.1.2 on 2025-02-22 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_group_class_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='students',
            field=models.ManyToManyField(related_name='students', to='group.student'),
        ),
    ]
