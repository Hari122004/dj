# project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('homepage.urls')),
    path('A/',include('member.urls')),
   ]
