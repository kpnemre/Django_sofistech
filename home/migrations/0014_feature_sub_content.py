# Generated by Django 3.0.7 on 2020-06-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200627_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='sub_content',
            field=models.CharField(default=1, max_length=150, verbose_name='üst içerik'),
            preserve_default=False,
        ),
    ]