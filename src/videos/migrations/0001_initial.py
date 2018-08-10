# Generated by Django 2.0.1 on 2018-08-10 13:29

from django.db import migrations, models
import videokit.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', videokit.models.VideoField(blank=True, duration_field='video_duration', height_field='video_height', mimetype_field='video_mimetype', null=True, rotation_field='video_rotation', thumbnail_field='video_thumbnail', upload_to='video/', width_field='video_width')),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateTimeField(blank=True, verbose_name='published date')),
                ('video_width', models.IntegerField(blank=True, null=True)),
                ('video_height', models.IntegerField(blank=True, null=True)),
                ('video_rotation', models.FloatField(blank=True, null=True)),
                ('video_mimetype', models.CharField(blank=True, max_length=32, null=True)),
                ('video_duration', models.IntegerField(blank=True, null=True)),
                ('video_thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('shared', models.BooleanField(default=True)),
            ],
        ),
    ]
