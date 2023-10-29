from django.db import models
from embed_video.fields import EmbedVideoField

class tutorial(models.Model):
    tutorial_Title = models.CharField(max_length=200)
    tutorial_Body = models.TextField()
    tutorial_Video = EmbedVideoField()
    tutorial_image = models.URLField(max_length=200)  # Add the image URL field

    class Meta:
        verbose_name_plural = "Tutorials"

    def __str__(self):
        return str(self.tutorial_Title) if self.tutorial_Title else " "
