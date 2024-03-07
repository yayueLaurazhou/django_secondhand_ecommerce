from django.urls import path
from . import views


app_name = "userProfile"
urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("newitem/", views.new, name="new"),
    path("edit/<int:pk>/", views.edit, name="edit"),
    path("delete/<int:pk>", views.delete, name="delete")
]
