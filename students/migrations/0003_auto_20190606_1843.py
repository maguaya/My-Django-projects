# Generated by Django 2.2.1 on 2019-06-06 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20190530_2158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='registation_number',
            new_name='registration_number',
        ),
    ]
