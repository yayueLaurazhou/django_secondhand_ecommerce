from django.urls import path

from . import views

app_name = 'productDetails'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
]