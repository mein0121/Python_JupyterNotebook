from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser



# UserAdmin: 관리자앱에서 사용자 관리 화면.
class CustomUserAdmin(UserAdmin):
    UserAdmin.fieldsets[1][1]['fields']=('name','email','gender')
    
    list_display = ['username', 'name','email']
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)