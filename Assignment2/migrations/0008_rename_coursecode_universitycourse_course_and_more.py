# Generated by Django 5.1.3 on 2024-12-01 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Assignment2', '0007_alter_university_universityid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='universitycourse',
            old_name='CourseCode',
            new_name='Course',
        ),
        migrations.RenameField(
            model_name='universitycourse',
            old_name='UniversityID',
            new_name='University',
        ),
    ]