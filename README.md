# Yandex.Afisha — Интерактивная карта интересных мест 
Учебный проект на Django: сайт-карта с достопримечательностями, реализованный для закрепления навыков разработки современных веб-приложений.

Ссылка на рабочий [сайт](https://maksimoboznyi.pythonanywhere.com/)

##  Как запустить проект локально

1. **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/MaksimObozniy/Yandex.Afisha.git
    cd Yandex.Afisha
    ```

2. **Установите зависимости:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Создайте файл `.env` в корне:**
    ```env
    DJANGO_SECRET_KEY=ваш-secret-key
    DJANGO_DEBUG=True (Прописывать это не обязательно, автоматически будет False)
    PROJECT_ALLOWED_HOSTS=localhost,127.0.0.1
    ```
    DJANGO_SECRET_KEY — секретный ключ Django. Используется для криптографических подписей. Должен быть уникальным и храниться в секрете.

    DJANGO_DEBUG — режим отладки (True/False). Если указать True, проект запустится в debug-режиме с подробными ошибками. По умолчанию False (безопасный режим для продакшена).

    PROJECT_ALLOWED_HOSTS — список разрешённых хостов (через запятую), с которых может работать сайт. По умолчанию: localhost. Подробнее: Django docs: [ALLOWED_HOSTS] (https://docs.djangoproject.com/en/4.2/ref/settings/#allowed-hosts)

4. **Выполните миграции:**
    ```bash
    python manage.py migrate
    ```

5. **Создайте суперпользователя (для входа в админку):**
    ```bash
    python manage.py createsuperuser
    ```

6. **Запустите сервер:**
    ```bash
    python manage.py runserver
    ```

## Добавление новой локации (Place)

### Через импорт jSON

Пример файла .json:

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [37.618423, 55.751244]
      },
      "properties": {
        "title": "Красная площадь",
        "description": "Главная площадь Москвы",
        "images": [
          "http://example.com/media/images/red_square_1.jpg"
        ]
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [30.31413, 59.93863]
      },
      "properties": {
        "title": "Дворцовая площадь",
        "description": "Центральная площадь Санкт-Петербурга"
      }
    }
  ]
}
```

#### Как импортировать данные из JSON сразу в бд:

для того чтобы импортировать место с фотографиями в БД, понадобиться в консоли прописать команду: 
```bash
python manage.py load_place (тут любой url который содержит json как показан сверху)
```

В процессе и поитогу после скачивания у вас появятся сообщения:

```bash
Создано место: Эйфелева башня в Москве
Загружено изображение: 8868d171420b5221f8f50af5e95a7b12.jpeg
Загружено изображение: 46cb25cf1719bf546c8bbcf1b51ba4f4.jpeg
Место "Эйфелева башня в Москве" загружено полностью!
```
