from django.contrib import admin
from .models import Buyer, Game

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'age_limited')  # Укажите поля, которые вы хотите отобразить в списке
    list_filter = ('cost', 'age_limited')  # Добавьте фильтр по цене и по ограничению возраста

# Регистрация модели Buyer в админке
admin.site.register(Buyer)

# Регистрация модели Game с кастомным классом администрирования
admin.site.register(Game, GameAdmin)