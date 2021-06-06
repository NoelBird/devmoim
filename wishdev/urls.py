from django.urls import path
from . import views

app_name = "wishdev"

urlpatterns = [
    path('whishdev/', views.index, name="index"),
    path('whishdev/create', views.create, name="create"),
]