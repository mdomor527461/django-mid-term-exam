# Generated by Django 5.0.6 on 2024-06-18 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
    ]
