# Generated by Django 5.0.1 on 2024-01-04 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classic_music_app', '0008_alter_music_melody'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='melody',
            field=models.FileField(null=True, upload_to='melody_images'),
        ),
    ]
