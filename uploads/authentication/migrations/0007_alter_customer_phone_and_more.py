# Generated by Django 4.0.4 on 2022-05-05 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='restaurentregister',
            name='contact',
            field=models.IntegerField(),
        ),
    ]
