from django.urls import path
from .views import GameListAPIView, GameUserListAPIView, GameDetail, GameUserDetail

urlpatterns = [
    path('games/', GameListAPIView.as_view(), name='games_list'),
    path('game_users/', GameUserListAPIView.as_view(), name='game_users_list'),
    path('games/<int:pk>/', GameDetail.as_view(), name='game_detail'),
    path('game_users/<int:pk>/', GameUserDetail.as_view(), name='game_user_detail'),
]
