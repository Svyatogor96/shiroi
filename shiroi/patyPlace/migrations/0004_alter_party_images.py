# Generated by Django 4.2 on 2023-04-15 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patyPlace', '0003_alter_party_creatorid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='images',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
