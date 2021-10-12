from django.urls import path
from . import views
urlpatterns = [
    path('', views.Login),
    path('home',views.home)
]
