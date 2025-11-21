from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as UserManager

@admin.register(User)
class UserAdmin(UserManager):
    list_display = ["username", "email", "phone", "is_staff"]
    search_fields = ["username", "email"]
    
    fieldsets = (
        ("Personal Info", {"fields":('username', 'email')}),
        (None, {"fields":("password", "phone")}),
        
    )
    add_fieldsets = (
        (None,{
            'classes':('wide'),
            'fields':('username', 'email', 'phone', 'password', 'Confirm password' , 'is_active', 'is_staff', 'is_superuser')
        }) ,       
    )
    