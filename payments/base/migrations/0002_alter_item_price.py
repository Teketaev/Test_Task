# Generated by Django 5.0.2 on 2024-03-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=20),
        ),
    ]
