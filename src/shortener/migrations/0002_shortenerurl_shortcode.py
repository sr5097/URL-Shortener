# Generated by Django 3.2.5 on 2021-07-11 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortenerurl',
            name='shortcode',
            field=models.CharField(default='urlshortener', max_length=15),
            preserve_default=False,
        ),
    ]
