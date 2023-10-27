from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='images')


    def __str__(self):
        return self.image



