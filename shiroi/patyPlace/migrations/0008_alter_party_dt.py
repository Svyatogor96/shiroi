# Generated by Django 4.2 on 2023-04-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patyPlace', '0007_alter_party_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='dt',
            field=models.DateField(max_length=20),
        ),
    ]
