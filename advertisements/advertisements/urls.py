from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_advertisements', include('app_advertisements.urls')),
    path('', include('app_lesson_4.urls')),
]
