from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email', 'roll']
    fieldsets = UserAdmin.fieldsets + (
        ("Extra Info", {"fields": ("phone_number","roll",)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)