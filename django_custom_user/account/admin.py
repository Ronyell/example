from django.contrib import admin
from .models import User, Company

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Company)
