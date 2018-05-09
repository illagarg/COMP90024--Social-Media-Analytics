# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Maps(models.Model):
	mapname= models.CharField(max_length=100)
	cityname=models.CharField(max_length=100)
	lat=models.CharField(max_length=10)
	lon=models.CharField(max_length=10)
	infotitle=models.CharField(max_length=100, default='')
	infomsg=models.CharField(max_length=100, default='')
	infotitle2=models.CharField(max_length=100, default='')
	infomsg2=models.CharField(max_length=100, default='')
	infotitle3=models.CharField(max_length=100, default='')
	infomsg3=models.CharField(max_length=100, default='')