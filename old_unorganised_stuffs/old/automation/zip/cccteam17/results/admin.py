# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Maps
from .models import Lists
# Register your models here.
admin.site.register(Maps)
admin.site.register(Lists)