from django.urls import path, include


from .views import ListLinks, DetailLink


urlpatterns = [
    path('<int:pk>/', DetailLink.as_view()),
    path('', ListLinks.as_view()),
]