from django.urls import path, include
from .views import ListLink, DetailLink, Userlist, UserDetail


urlpatterns = [
    path('<int:pk>/', DetailLink.as_view()),
    path('', ListLink.as_view()),
    path('users/', Userlist.as_view()),
    path('users/<int:pk>/', UserDetail.as_view())
]
