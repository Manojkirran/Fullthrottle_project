# Generated by Django 3.1.5 on 2021-02-11 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='id1',
            new_name='Emp_id',
        ),
    ]