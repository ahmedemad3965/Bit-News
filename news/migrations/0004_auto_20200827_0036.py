# Generated by Django 3.0.3 on 2020-08-27 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200825_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=1024, unique=True),
        ),
        migrations.AlterField(
            model_name='posttag',
            name='tag',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
