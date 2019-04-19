from django.contrib import admin
from .models import Login


class LoginAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'confirmPassword')


admin.site.register(Login, LoginAdmin)
