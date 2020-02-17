from . import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('vision/', views.add_image, name='vision'),
    path('', views.index, name='index'),
] 