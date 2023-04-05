import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Game, GameUser


class GameTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        """Начальные данные для класса GameTests"""
        cls.game = Game.objects.create(description='test', stage_number=3, stage_end_date='2023-12-12')

    def test_create_game(self):
        """Тест-метод создания игры"""
        url = reverse('games_list')
        data = {'description': 'test', 'stage_number': 3, 'stage_end_date': '12.12.2023'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content), {'id': 2, 'description': 'test', 'stage_number': 3,
                                                        'stage_end_date': '12.12.2023'})
        self.assertEqual(Game.objects.count(), 2)

    def test_get_games_list(self):
        """Тест-метод получения списка игр"""
        url = reverse('games_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_game(self):
        """Тест-метод для обновления игры"""
        url = reverse('game_detail', kwargs={'pk': self.game.pk})
        data = {'description': 'test_2', 'stage_number': 7, 'stage_end_date': '12.12.2023'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class GameUsersTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        """Начальные данные для класса GameUsersTests"""
        cls.game = Game.objects.create(description='test', stage_number=3, stage_end_date='2023-12-12')
        cls.user = GameUser.objects.create(name='test_user', stage_1=True, stage_2=False)
        cls.user.game.set([1])

    def test_game_users_list(self):
        """Тест-метод получения списка пользователей"""
        url = reverse('game_users_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        """Тест-метод создания пользователя"""
        url = reverse('game_users_list')
        data = {'name': 'test_user', 'stage_1': True, 'stage_2': False, 'game': [self.game.pk]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GameUser.objects.count(), 2)
        self.assertEqual(json.loads(response.content), {'user_id': 2, 'name': 'test_user', 'stage_1': True,
                                                        'stage_2': False,
                                                        'game': [self.game.pk]})

    def test_update_user(self):
        """Тест-метод для обновления данных о пользователе"""
        url = reverse('game_user_detail', kwargs={'pk': self.user.user_id})
        data = {'name': 'test_user2', 'stage_1': False, 'stage_2': True, 'game': [self.game.pk]}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
