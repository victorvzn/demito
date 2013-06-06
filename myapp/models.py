#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Amigo(models.Model):
    nombres = models.CharField(max_length=50)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.nombres