# Generated by Django 3.0.3 on 2020-06-24 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rev', '0002_auto_20200624_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pics/%y/%m/%d/', verbose_name='image'),
        ),
    ]