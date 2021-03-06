# Generated by Django 3.0.6 on 2020-05-23 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20200523_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='academic_sub_category',
            field=models.CharField(blank=True, choices=[('School Books', 'School Books'), ('High School Books', 'High School Books'), ('A Level Books', 'A Level Books'), ("Bachelor's Books", "Bachelor's Books"), ("Master's Books", "Master's Books")], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='nonacademic_sub_category',
            field=models.CharField(blank=True, choices=[('Novel', 'Novel'), ('Stories', 'Stories'), ('Poetry', 'Poetry'), ('Novel', 'Novel'), ('Essay', 'Essay'), ('Biography', 'Biography'), ('Auto Biography', 'Auto Biography'), ('Article', 'Article'), ('Travelouge', 'Travelouge')], max_length=50, null=True),
        ),
    ]
