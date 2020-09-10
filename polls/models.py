import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Entity(models.Model):
    entity_info = models.TextField()
    entity_text = models.CharField(max_length=200)
    entity_img = models.ImageField(upload_to='static/polls/', blank=True, null=True)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.entity_info

    def __str__(self):
        return self.entity_text

    @property
    def published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Info(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    info_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.info_text


