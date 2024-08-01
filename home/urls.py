from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header="MADNI INTER COLLEGE"
admin.site.site_title="MADNI INTER COLLEGE"
admin.site.index_title=" WELCOME TO MADNI INTER COLLEGE PORTAL"

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('academic_council',views.academic_council,name='academic_council'),
    path('career',views.career,name='career'),
    path('directors_message',views.directors_message,name='directors_message'),
    path('faculty',views.faculty,name='faculty'),
    path('faq',views.faq,name='faq'),
    path('form',views.form,name='form'),
    path('gallery',views.gallery,name='gallery'),
    path('library',views.library,name='library'),
    path('rti',views.rti,name='rti'),
    path('student_corner',views.student_corner,name='student_corner'),
    path('initial',views.initial,name='initial'),
    path('time_table',views.time_table,name='time_table'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    