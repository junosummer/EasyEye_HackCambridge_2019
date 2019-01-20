# Generated by Django 2.1.3 on 2019-01-20 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alert'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='alert_level',
        ),
        migrations.AddField(
            model_name='alert',
            name='alert_blink_slow',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alert',
            name='alert_blur_sight',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alert',
            name='alert_usage_overtime',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alert',
            name='alert_wrong_direction',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='seconddata',
            name='direction',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='seconddata',
            name='squint',
            field=models.FloatField(default=0),
        ),
    ]
