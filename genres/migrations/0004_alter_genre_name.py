# Generated by Django 5.1.3 on 2024-11-14 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0003_genre_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
