# Generated by Django 2.2 on 2020-04-22 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_auto_20200422_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
