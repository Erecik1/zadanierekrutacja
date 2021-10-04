# Generated by Django 3.2.7 on 2021-10-03 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20211004_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='link_to_cover',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='number_of_pages',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
