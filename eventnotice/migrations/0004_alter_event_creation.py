# Generated by Django 3.2.6 on 2021-09-08 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventnotice', '0003_auto_20210909_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='creation',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
