# Generated by Django 2.2.6 on 2019-10-07 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='nickname',
            field=models.CharField(default='', max_length=20),
        ),
    ]