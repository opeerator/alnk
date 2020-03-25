from django.urls import path, include


from .views import ListLink, DetailLink


urlpatterns = [
    path('<int:pk>/', DetailLink.as_view()),
    path('', ListLink.as_view()),
]
