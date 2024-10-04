from django.urls import path
from testapp import views


urlpatterns=[
    path('test/',views.test,name='testapp'),#функция path прокладывает маршрут к test из файла views по адресу https://localhost:8000/test
]