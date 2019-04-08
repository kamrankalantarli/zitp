# Generated by Django 2.1.5 on 2019-01-24 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Başlıq')),
                ('content', models.TextField(blank=True, verbose_name='Xəbər')),
                ('publish', models.DateTimeField(auto_now=True, verbose_name='Tarix')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'ordering': ['-publish', 'id'],
            },
        ),
    ]
