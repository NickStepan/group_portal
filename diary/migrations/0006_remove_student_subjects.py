# Generated by Django 5.1.2 on 2025-02-14 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0005_remove_diary_teacher_remove_student_subjects_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='subjects',
        ),
    ]
