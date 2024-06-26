from django.contrib import admin
from accounts.models import CustomUser, UserAnswer

# Register your models h
admin.site.register(CustomUser)
admin.site.register(UserAnswer)
