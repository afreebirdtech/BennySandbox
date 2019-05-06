from django.contrib import admin
from .models import User
from .models import Usertype, Program
# Register your models here.

admin.site.register(User)
admin.site.register(Usertype)
admin.site.register(Program)
