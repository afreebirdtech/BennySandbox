from django.contrib import admin
from .models import User
from .models import Usertype, Program, ArtArea, Household,Tutor
# Register your models here.

admin.site.register(User)
admin.site.register(Tutor)
admin.site.register(Usertype)
admin.site.register(Program)
admin.site.register(ArtArea)
admin.site.register(Household)

