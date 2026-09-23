# BlogAPI

Пет-проект для изучения DRF, выполненный по руководству Уильяма С. Виснсента "Django for APIs".

## Технологии

- Python
- Django
- Django REST Framework
- dj-rest-auth / django-allauth
- drf-spectacular
- django-cors-headers
- environs
- SQLite / PostgreSQL (psycopg)
- whitenoise
- gunicorn
- ruff
- uv

## Развёртывание

### Клонирование репозитория

```bash
git clone <repo-url>
cd BlogAPI
```

### Docker

Настройка окружения:

```bash
cp .env.example .env
```

```bash
docker compose up --build
```

### Локально

Установка зависимостей:

```bash
uv sync
```

Настройка окружения (создать файл `.env` в корне проекта):

```
DJANGO_SECRET_KEY=<секретный ключ>
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

Применение миграций:

```bash
uv run python manage.py migrate
```

Запуск сервера:

```bash
uv run python manage.py runserver
```

API будет доступно по адресу:

```
http://localhost:8000/api/v1/
```

Документация:

```
http://localhost:8000/api/schema/swagger/
http://localhost:8000/api/schema/redoc/
```

## Запуск тестов

```bash
uv run python manage.py test
```

## API

### Аутентификация (dj-rest-auth / allauth)

- `POST /api/v1/dj_rest_auth/login/` — вход
- `POST /api/v1/dj_rest_auth/logout/` — выход
- `POST /api/v1/dj_rest_auth/registration/` — регистрация нового пользователя

### Пользователи

- `GET /api/v1/users/` — список пользователей (только для администраторов)
- `GET /api/v1/users/{id}/` — данные пользователя

### Посты

- `GET /api/v1/` — список постов
- `POST /api/v1/` — создание поста (автором становится текущий пользователь)
- `GET /api/v1/{id}/` — пост по id
- `PATCH /api/v1/{id}/` — редактирование поста (только автор)
- `DELETE /api/v1/{id}/` — удаление поста (только автор)

## Структура проекта

- `manage.py` — точка входа Django-приложения
- `django_project/` — настройки проекта, `urls.py`, `wsgi.py`/`asgi.py`
- `accounts/` — кастомная модель пользователя (`CustomUser`), формы, админка
- `posts/` — модель поста, сериализаторы, разрешения, вьюсеты, роуты
- `static/` — исходные статические файлы
- `staticfiles/` — собранные статические файлы (`collectstatic`, в git не хранится)
- `schema.yml` — экспортированная OpenAPI-схема (drf-spectacular)
- `requirements.txt`, `pyproject.toml`, `uv.lock` — зависимости проекта
- `Dockerfile`, `docker-compose.yml` — контейнеризация
