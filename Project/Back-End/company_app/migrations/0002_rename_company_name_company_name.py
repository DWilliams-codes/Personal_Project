# Generated by Django 4.2.3 on 2023-08-15 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='company_name',
            new_name='name',
        ),
    ]