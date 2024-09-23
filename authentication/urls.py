from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('success/', views.success_view, name="success"),
    path('s/', views.s_view, name="s"),
]