from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register([Role , Department , Location , User , UserDocument])
