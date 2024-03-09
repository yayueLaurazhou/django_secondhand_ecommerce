from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('chat/<int:pk>', views.chat, name='chat'),
    path('getMessages/', views.getMessages, name='getMessages'),
]
