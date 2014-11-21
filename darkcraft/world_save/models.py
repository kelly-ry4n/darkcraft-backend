from django.db import models
from django.utils import timezone
# Create your models here.
class WorldSave(models.Model):
    date = models.DateTimeField(blank=True)
    signature = models.CharField(max_length=255)
    compressed_file = models.FileField(blank=True,null=True)
    ip = models.CharField(max_length=255,blank=True)

    def save(self,*args, **kwargs):
        if not self.id:
            self.date = timezone.now()
        return super(WorldSave, self).save(*args, **kwargs)
