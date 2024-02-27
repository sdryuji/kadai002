from django.contrib import admin
from .models import AdminUser, CustomUser, GeneralUser, StoreUser

admin.site.register(CustomUser)
admin.site.register(StoreUser)
admin.site.register(GeneralUser)
admin.site.register(AdminUser)
