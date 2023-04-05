from django.http import JsonResponse, Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import GameSerializer, GameUserSerializer
from .models import Game, GameUser
from django.core.cache import cache

CACHE_TIME = 60 * 60 * 2


class GameListAPIView(APIView):
    """APIView для списка игр"""

    def get(self, request):
        queryset = Game.objects.all()
        data = cache.get_or_set('games_list', queryset, CACHE_TIME)
        return JsonResponse(GameSerializer(data, many=True).data, safe=False)

    def post(self, request):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            cache.delete('games_list')
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class GameUserListAPIView(APIView):
    """APIView для списка пользователь"""

    def get(self, request):
        queryset = GameUser.objects.all()
        data = cache.get_or_set('game_users_list', queryset, CACHE_TIME)
        return JsonResponse(GameUserSerializer(data, many=True).data, safe=False)

    def post(self, request):
        serializer = GameUserSerializer(data=request.data)
        if serializer.is_valid():
            cache.delete('game_users_list')
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class GameDetail(APIView):
    """Детальнон представление игры"""

    def get_object(self, pk):
        try:
            instance = Game.objects.get(pk=pk)
            return instance
        except Game.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        game = self.get_object(pk)
        data = cache.get_or_set(f'game_{pk}', game, CACHE_TIME)
        return JsonResponse(GameSerializer(data).data, safe=False)

    def put(self, request, pk):
        instance = self.get_object(pk)
        serializer = GameSerializer(instance, data=request.data)
        if serializer.is_valid():
            cache.delete(f'game_{pk}')
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class GameUserDetail(APIView):
    """Деиальное представление пользователя"""

    def get_object(self, pk):
        try:
            instance = GameUser.objects.get(pk=pk)
            return instance
        except GameUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        game_user = self.get_object(pk)
        data = cache.get_or_set(f'game_user_{pk}', game_user, CACHE_TIME)
        return JsonResponse(GameUserSerializer(data).data, safe=False)

    def put(self, request, pk):
        instance = self.get_object(pk)
        serializer = GameUserSerializer(instance, data=request.data)
        if serializer.is_valid():
            cache.delete(f'game_user_{pk}')
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
