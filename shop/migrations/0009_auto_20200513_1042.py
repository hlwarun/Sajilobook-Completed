# Generated by Django 3.0.6 on 2020-05-13 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20200513_1019'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('title', 'product_code')},
        ),
    ]
