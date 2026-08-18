# Pets — Сайт для владельцев домашних животных 🐾

Веб-приложение, созданное для помощи владельцам домашних животных. Проект переведен на фреймворк **Django (Python)**, имеет правильную модульную структуру приложений и готов к расширению функционала (база данных питомцев, личные кабинеты, каталог аксессуаров и питания).

## 🛠 Стек технологий
* **Backend:** Python 3.14+ / Django 6.1
* **Frontend:** HTML5, CSS3, JavaScript

## 🚀 Как запустить проект локально

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com
   cd pets
   ```

2. **Создайте и активируйте виртуальное окружение:**
   * **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   * **macOS / Linux:**
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

3. **Установите необходимые зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Выполните миграции базы данных:**
   ```bash
   python manage.py migrate
   ```

5. **Запустите сервер разработки:**
   ```bash
   python manage.py runserver
   ```
   После этого сайт будет доступен по адресу: http://127.0.0
