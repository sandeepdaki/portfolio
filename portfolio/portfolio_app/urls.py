from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name="home"),
    path('wheter/',views.wheter, name="wheter"),
    path('portfolio/',views.portfolio, name="portfolio")
]
