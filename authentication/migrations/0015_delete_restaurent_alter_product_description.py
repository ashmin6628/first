# Generated by Django 4.0.4 on 2022-05-06 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0014_restaurent_address_alter_restaurent_contact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Restaurent',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
    ]