# Generated by Django 4.0.5 on 2022-06-10 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_time',
            field=models.DateTimeField(verbose_name='Time'),
        ),
    ]
