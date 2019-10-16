from django.contrib import admin

# Register your models here.
from .models import Workshop

# destructute the thngs that are displayed
class WorkshopAdmin(admin.ModelAdmin):
    workshop_display=('id','title','venue','city','is_published','price','workshop_date','facilitator')
    workshop_display_links=('id','title')
    workshop_filter=('facilitator',)
    workshop_editable=('is_published',)
    search_fields=('id','title','venue','city')

admin.site.register(Workshop, WorkshopAdmin)

