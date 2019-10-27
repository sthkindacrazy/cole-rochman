# Generated by Django 2.2.6 on 2019-10-27 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_add_patients_columns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='next_visiting_date',
            field=models.DateTimeField(default=None, null=True, verbose_name='다음 내원일'),
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='next_visiting_date',
            new_name='next_visiting_date_time'
        )
    ]
