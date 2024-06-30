from django.contrib import admin

from .models import IceCream, IceCreamKiosk, Parent, Child

# Register your models here.


admin.site.register(IceCreamKiosk)
admin.site.register(IceCream)

admin.site.register(Parent)
admin.site.register(Child)