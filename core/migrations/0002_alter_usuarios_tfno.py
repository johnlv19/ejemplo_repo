# Generated by Django 4.1.5 on 2023-02-01 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='tfno',
            field=models.CharField(max_length=10),
        ),
    ]
