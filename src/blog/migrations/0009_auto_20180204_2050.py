# Generated by Django 2.0.1 on 2018-02-04 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180204_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='custom_scripts',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='custom_styles',
            field=models.TextField(blank=True, null=True),
        ),
    ]