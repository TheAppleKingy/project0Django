from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

# Create your views here.
def other_adress(request,year):             #redirect()-функция, которая перенаправляет на указанный первым параметром адрес(можно засунуть вьюшку или лучше всего имя маршрута)
    if year==2025:                          #permanent отвечает за то временно ли была перемещена страница или на все время. в данном примере нас будет 
        return redirect('home',permanent=False)#перенаправлять на главную страницу если выполнится первое условие(укажем тут имя home маршрута главной страницы)
    elif year>=2026:
        return HttpResponseNotFound('<h1>NotFound<h1>')#страницы с параметром >=2026 не будут найдены
    return render(request,'other_adress/randompictures.html')#параметр year в этой вьюшке находится сразу после request а именно после http://127.0.0.1:8000/othadr/                                            