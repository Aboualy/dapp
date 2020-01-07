from django.urls import path
from .views import (
    GameListView,
    GameDetailView,
    GameCreateView,
    GameUpdateView,
    GameDeleteView
)
from . import views

urlpatterns = [
    path('home/', GameListView.as_view(), name='home-page'),
    path('game/<int:pk>/', GameDetailView.as_view(), name='game-detail'),
    path('game/new/', GameCreateView.as_view(), name='game-create'),
    path('game/<int:pk>/update/', GameUpdateView.as_view(), name='game-update'),
    path('game/<int:pk>/delete/', GameDeleteView.as_view(), name='game-delete'),
    path('about/', views.about, name='about-us'),
]