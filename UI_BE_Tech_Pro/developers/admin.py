from django.contrib import admin

# Register your models here.
from .models import Developers


class DevelopersAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'user',
                    'designation',
                    'total_experience',
                    'employment_type',
                    'location',
                    'annual_ctc',
                    'linked_in_profile',
                    'start_date',
                    'end_date']

admin.site.register(Developers, DevelopersAdmin)