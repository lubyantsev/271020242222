from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif Buyer.objects.filter(name=username).exists():  # Проверяем существование покупателя
                info['error'] = 'Покупатель с таким именем уже существует'
            else:
                # Сохранение нового покупателя
                Buyer.objects.create(name=username, balance=0, age=age)  # Создаем покупателя
                return render(request, 'first_task/registration_page.html', {'message': f'Приветствуем, {username}!'})

    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'first_task/registration_page.html', info)


def sign_up_by_html(request):
    return sign_up_by_django(request)  # Можно использовать одну и ту же функцию


# Новые функции
def home(request):
    return render(request, 'first_task/home.html')


def shop(request):
    games = Game.objects.all()  # Получаем все записи из модели Game
    return render(request, 'first_task/shop.html', context={'games': games})


def cart(request):
    return render(request, 'first_task/cart.html')
