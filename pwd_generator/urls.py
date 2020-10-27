
from django.contrib import admin
from django.urls import path
import generator.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',generator.views.home, name='home'),
    path('password/',generator.views.password, name='password'),
]
