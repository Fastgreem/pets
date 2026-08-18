from django.contrib import admin
from django.urls import path
from main import views  # Импортируем логику из нашего приложения main

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "", views.home, name="home"
    ),  # Главная страница (пустые кавычки '' означают корень сайта)
]
