from django.db import models
from django.utils import timezone
# Create your models here.

class MapRender(models.Model):

    ip = models.CharField(max_length=255)
    start = models.DateTimeField()

    def save(self, *args, **kwargs):

        self.date = timezone.now()
        super(MapRender,self).save(*args, **kwargs)