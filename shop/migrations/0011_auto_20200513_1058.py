# Generated by Django 3.0.6 on 2020-05-13 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20200513_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='active',
            new_name='available_in_stock',
        ),
    ]
