from django.db import models

# Create your models here.
class attributes(models.Model):
    path = models.CharField(max_length=255)
    file_name = models.CharField(max_length=128)
    size = models.BigIntegerField()
    file_type = models.CharField(max_length=20)
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    access_time = models.DateTimeField()
    def __unicode__(self):
        return "{}/{} - {}".format(self.path, self.file_name, self.moified_time)