#в этом файле можно прописать все маршруты связанные с приложением mainstr и разом добавить в urls в пакете конфигураций
from django.urls import path
from mainstr import views


urlpatterns = [
    path('',views.main,name='home'),#тут у нас главная страница по адресу https://localhost:8000
]