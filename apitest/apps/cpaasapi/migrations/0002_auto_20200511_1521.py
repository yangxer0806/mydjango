# Generated by Django 3.0.3 on 2020-05-11 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpaasapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paas',
            name='playDelay',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='paas',
            name='playTimes',
            field=models.IntegerField(),
        ),
    ]