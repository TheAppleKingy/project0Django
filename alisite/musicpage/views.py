from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def music(request):
    print(request.GET)#тут мы печатаем все параметры(ключ-значение), полученные в url. например в  http://127.0.0.1:8000/music/?author=Shakira&song=crazy
    return render(request,'musicpage/music.html')#в данном случае выведет <QueryDict: {'author': ['Shakira'], 'song': ['crazy']}>