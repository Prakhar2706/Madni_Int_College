from django.contrib import admin
from home.models import Event
from home.models import News
from home.models import Announcement
from home.models import Floating
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display=('Event_date','Event_month','Event_des')
admin.site.register(Event,EventAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display=('News_name','News_des')
admin.site.register(News,NewsAdmin)

class AnnouncementAdmin(admin.ModelAdmin):
    list_display=('Announcement_name','Announcement_des')
admin.site.register(Announcement,AnnouncementAdmin)

class FloatingAdmin(admin.ModelAdmin):
    list_display=['Floating_img']
    ordering=('Floating_img',)
admin.site.register(Floating,FloatingAdmin)          

