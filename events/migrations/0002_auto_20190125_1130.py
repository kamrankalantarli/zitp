# Generated by Django 2.1.5 on 2019-01-25 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='publish',
            field=models.DateTimeField(verbose_name='Tarix'),
        ),
    ]
