from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Game, GameUser


class GameSerializer(ModelSerializer):

    stage_end_date = serializers.DateField(format='%d.%m.%Y')

    class Meta:
        model = Game
        fields = ['id', 'description', 'stage_number', 'stage_end_date']


class GameUserSerializer(ModelSerializer):
    class Meta:
        model = GameUser
        fields = ['user_id', 'name', 'stage_1', 'stage_2', 'game']
