from django.contrib import admin

# Register your models here.
from .models import Designation, TechStack, User, EmploymentType


class DesignationAdmin(admin.ModelAdmin):
    list_display = ['designation']

class TechStackAdmin(admin.ModelAdmin):
    list_display = ['tech_stack']

class EmploymentTypeAdmin(admin.ModelAdmin):
    list_display = ['employment_type']

class UserAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Designation,DesignationAdmin)
admin.site.register(TechStack,TechStackAdmin)
admin.site.register(EmploymentType,EmploymentTypeAdmin)
admin.site.register(User,UserAdmin)