# Generated by Django 5.1.2 on 2024-10-27 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0004_auto_20241026_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='paginas',
            field=models.PositiveIntegerField(db_index=True),
        ),
    ]
