# Generated by Django 3.0.2 on 2020-01-10 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitar',
            name='image',
            field=models.CharField(default='www.google.com', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rental',
            name='image',
            field=models.CharField(default='www.google.com', max_length=255),
            preserve_default=False,
        ),
    ]
