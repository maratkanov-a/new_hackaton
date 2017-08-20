# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from front_site.models import User, Company, Events

admin.site.register(User)
admin.site.register(Company)
admin.site.register(Events)