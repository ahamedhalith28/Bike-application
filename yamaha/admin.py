from django.contrib import admin
from .models import Variants, Role, Registration
# Register your models here.


admin.site.register(Role)
admin.site.register(Registration)
admin.site.register(Variants)
#dmin.site.register(User_list)