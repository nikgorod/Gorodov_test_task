# Тестовое задание "Brand Games"

Выполнил: Городов Никита.

## Инструкция по развертыванию на сервере

1. Клонировать репозиторий <br>
    `git clone `
2. Установить необходимые пакеты <br>
    `pip install requirements.txt`
3. Перейти в папку с проектом<br>
    `cd game_api`
4. Выполнить миграции<br>
    `python manage.py migrate`
5. Также возможно загрузить фиксутры <br>
    `python manage.py loaddata games.json` <br>
    `python manage.py loaddata game_users.json`
6. Запустить автотесты <br>
    `python manage.py test`
7. Запустить сервер <br>
   `python manage.py runserver`

### Тестируем наш API с помощью  httpie

Httpie - это удобный HTTP-клиент, написанный на Python

1. `http POST http://127.0.0.1:8000/api/games/ description='game_test' stage_number=3 stage_end_date='12.04.2023'`
2. `http GET http://127.0.0.1:8000/api/games/`
3. `http POST http://127.0.0.1:8000/api/game_users/ name='game_user_2' stage_1:=true stage_2:=false game:='[game_id]'`
4. `http GET http://127.0.0.1:8000/api/game_users/<int:user_id>/`
5. `http PUT http://127.0.0.1:8000/api/game_users/<int:user_id>/ name='test_user10' stage_1:=true stage_2:=false game:='[game_id]'`
6. `http GET http://127.0.0.1:8000/api/game_users/`