# Generated by Django 3.2 on 2023-02-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20230201_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.CharField(max_length=255),
        ),
    ]
