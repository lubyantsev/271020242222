from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)  # Имя покупателя
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Баланс
    age = models.PositiveIntegerField()  # Возраст

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)  # Название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    size = models.DecimalField(max_digits=10, decimal_places=2)  # Размер файлов игры
    description = models.TextField()  # Описание
    age_limited = models.BooleanField(default=False)  # Ограничение возраста
    buyers = models.ManyToManyField(Buyer, related_name='games')  # Покупатели

    def __str__(self):
        return self.title


class Order(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)  # Связь с покупателем
    game = models.ForeignKey(Game, on_delete=models.CASCADE)  # Связь с игрой
    order_date = models.DateTimeField(auto_now_add=True)  # Дата заказа
    quantity = models.PositiveIntegerField()  # Количество

    def __str__(self):
        return f"Order {self.id} by {self.buyer.name} for {self.quantity} of {self.game.title}"


class Review(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)  # Связь с покупателем
    game = models.ForeignKey(Game, on_delete=models.CASCADE)  # Связь с игрой
    rating = models.PositiveIntegerField()  # Оценка от 1 до 5
    comment = models.TextField()  # Комментарий

    def __str__(self):
        return f"Review by {self.buyer.name} for {self.game.title} - Rating: {self.rating}"