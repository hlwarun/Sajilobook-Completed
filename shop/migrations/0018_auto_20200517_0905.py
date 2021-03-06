# Generated by Django 3.0.6 on 2020-05-17 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20200517_0904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='slug',
            new_name='product_code',
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('title', 'product_code')},
        ),
    ]
