from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('newchat/<int:pk>/', views.new_chat, name="newchat"),
    path('chat/<int:pk>/', views.chat, name='chat'),
    path('getMessages/<int:pk>', views.getMessages, name='getMessages'),
]
