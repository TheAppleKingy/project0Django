from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def test(request):#это функция-представление. в ответ на запрос request с сервера в ответ приходит данное представление. тут это будет страница с
                  #одной строкой, но вообще html страница. далее мы должны прроложить маршрут к этому представлению в файле urls.py
    return render(request,'testapp/test.html')