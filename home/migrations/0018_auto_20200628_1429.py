# Generated by Django 3.0.7 on 2020-06-28 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20200628_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reference',
            name='slug',
        ),
        migrations.AddField(
            model_name='reference',
            name='company_type',
            field=models.CharField(default=1, max_length=10, verbose_name='Filtreleme başlıkları'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reference',
            name='content',
            field=models.CharField(max_length=75, verbose_name='Referansın kısa açıklaması:'),
        ),
        migrations.AlterField(
            model_name='reference',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Referans resmi'),
        ),
        migrations.AlterField(
            model_name='reference',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Referansın adı:'),
        ),
    ]
