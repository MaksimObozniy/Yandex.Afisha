# Yandex.Afisha — Интерактивная карта интересных мест 
Учебный проект на Django: сайт-карта с достопримечательностями, реализованный для закрепления навыков разработки современных веб-приложений.

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
    SECRET_KEY=ваш-secret-key
    DEBUG=True
    ```

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
