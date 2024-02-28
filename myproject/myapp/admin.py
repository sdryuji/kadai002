from django.contrib import admin
from .models import Administrator, CustomUser, GeneralUser, StoreDetail, StoreUser

admin.site.register(CustomUser)
admin.site.register(StoreUser)
admin.site.register(GeneralUser)
admin.site.register(Administrator)
admin.site.register(StoreDetail)
