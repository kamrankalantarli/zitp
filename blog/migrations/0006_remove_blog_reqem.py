# Generated by Django 2.1.5 on 2019-01-25 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190124_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='reqem',
        ),
    ]
