# Generated by Django 4.2 on 2023-04-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patyPlace', '0006_alter_party_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='title',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
