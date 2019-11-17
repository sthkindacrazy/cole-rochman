# Generated by Django 2.2.6 on 2019-11-17 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_field_status_updated_at_on_notificationrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicationresult',
            name='severity',
            field=models.IntegerField(null=True, verbose_name='이상 정도'),
        ),
        migrations.AddField(
            model_name='medicationresult',
            name='status_info',
            field=models.TextField(default='', verbose_name='이상 종류'),
        ),
        migrations.AlterField(
            model_name='medicationresult',
            name='notified_at',
            field=models.DateTimeField(null=True),
        ),
    ]
