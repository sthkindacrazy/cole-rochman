# Generated by Django 2.2.6 on 2019-10-15 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_patient_hospital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='kakao_user_id',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]