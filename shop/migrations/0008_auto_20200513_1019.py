# Generated by Django 3.0.6 on 2020-05-13 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200513_0852'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='slug',
            new_name='product_code',
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set(),
        ),
    ]
