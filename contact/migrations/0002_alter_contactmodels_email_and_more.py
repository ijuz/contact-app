# Generated by Django 5.0 on 2023-12-12 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodels',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='contactmodels',
            name='phone_number',
            field=models.CharField(max_length=17),
        ),
    ]