# Generated by Django 3.0.7 on 2020-06-27 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_setting_featers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='featers',
            field=models.BooleanField(default=False, verbose_name='Özellikler kısmının gözükmesini istiyorsanız tıklayınız:'),
        ),
    ]