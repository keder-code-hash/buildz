# Generated by Django 3.2 on 2023-02-06 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_messageseenmetric'),
    ]

    operations = [
        migrations.AddField(
            model_name='messageseenmetric',
            name='message_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
