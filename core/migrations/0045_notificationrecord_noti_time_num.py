# Generated by Django 2.2.6 on 2019-11-26 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_auto_20191125_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationrecord',
            name='noti_time_num',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]