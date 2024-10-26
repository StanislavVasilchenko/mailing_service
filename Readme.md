# Шаги запуска

### 1) Установка зависимостей
```
pip install -r requirements.txt
```

### 2) Создать .env файл согласно .env.sample
### 3) Запустить фаил main.py
### 3) Запустить celery
```
celery -A src.tasks.settings:celery_app worker --loglevel=INFO

```
