from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.index_view, name="index"),
    path('add/', views.add_view, name="add"),
    path('leave/<int:group_id>', views.leave_view, name="leave"),
    path('join/<int:group_id>', views.join_view, name="join"),
    path('message/', views.message_view, name="message"),
    path('message/send', views.message_send_view, name="message_send"),
]