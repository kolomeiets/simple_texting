from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.index_view, name="index"),
    path('add/', views.add_view, name="add"),
]