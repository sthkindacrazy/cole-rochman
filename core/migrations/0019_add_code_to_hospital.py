# Generated by Django 2.2.6 on 2019-11-04 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_delete_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='code',
            field=models.CharField(default='A001', max_length=4, unique=True),
            preserve_default=False,
        ),
    ]
