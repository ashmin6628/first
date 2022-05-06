# Generated by Django 4.0.4 on 2022-05-05 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_restaurent'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurent',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='restaurent',
            name='contact',
            field=models.CharField(max_length=10),
        ),
    ]