from django.db import models
from django.utils import timezone

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s %s' % (self.title, self.body)

class Token(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    owner = models.CharField(max_length=200)
    expiration_datetime = models.DateTimeField(default=(timezone.now()+timezone.timedelta(days=7)))

    def __str__(self):
        return '%s    owned by %s      (%s)      status:%s     will expire:(%s)' % (self.id,
                                                                                    self.owner,
                                                                                    self.created_at,
                                                                                    self.status,
                                                                                    self.expiration_datetime)
