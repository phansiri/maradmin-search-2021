# Generated by Django 3.1.7 on 2021-10-22 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0004_auto_20211021_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maradmin',
            name='number',
            field=models.CharField(max_length=50),
        ),
    ]