from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

class Compositor(models.Model):
    fullname = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to = "images", verbose_name = "avatar")
    about = models.TextField()
    wikimedia = models.URLField()
    song_count = models.IntegerField(default=0)
    registered_time = models.DateField(auto_now=True)


    def __str__(self):
        return str(f'{self.fullname}')


    class Meta:
        verbose_name_plural = 'Compositors'

class Music(models.Model):
    property = models.ForeignKey(Compositor, on_delete = models.CASCADE, blank = True)
    title = models.CharField(max_length = 100, blank = True)
    music = models.FileField(upload_to = "musics",verbose_name = "Saz")
    music_image = models.ImageField(upload_to = "video_images", verbose_name = "Image of music", blank=True)
    melody = models.FileField(upload_to = "melody_images",null=True)
    duration = models.DurationField(default = datetime.timedelta(seconds = 0))
    uploaded_time = models.DateField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.music_image:
            self.music_image = 'images/music-notes-scores.jpg'
        super().save(*args, **kwargs)
        compositor = self.property
        compositor.song_count = Music.objects.filter(property=compositor).count()
        compositor.save()