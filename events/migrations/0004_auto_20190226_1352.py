# Generated by Django 2.1.5 on 2019-02-26 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190125_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventa',
            name='title',
            field=models.CharField(max_length=80, verbose_name='Başlıq'),
        ),
    ]
