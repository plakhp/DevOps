# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models


# Create your models here.
class user_info(models.Model):
    username = models.CharField(max_length=32)
    passwd = models.CharField(max_length=32)
