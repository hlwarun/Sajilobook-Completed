# Generated by Django 3.0.6 on 2020-05-16 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_sell'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='academic_subcategory',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sell',
            name='non_academic_subcategory',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
