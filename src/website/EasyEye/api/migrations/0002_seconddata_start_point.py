# Generated by Django 2.1.3 on 2019-01-19 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seconddata',
            name='start_point',
            field=models.BooleanField(default=False),
        ),
    ]
