from django.shortcuts import render

# Create your views here.

data_db=[

    {'id':1,'title':'Category 1','content':'descr1','published_status':True},
    {'id':2,'title':'Category 2','content':'descr2','published_status':False},
    {'id':3,'title':'Category 3','content':'descr2','published_status':True},
]
menu=['Зарегистрирвоаться','О нас','Пользовательское соглашение']

def categories(request):
    data={
        'title':'Main Page',
        'menu':menu,
        'posts':data_db,
    }
    # htmlpattern=render_to_string('mainstr/test.html')
    # return HttpResponse(htmlpattern)
    return render(request,'categories/categories.html',context=data)#выдаем шаблон html на запрос. данная строка равноценна двум предыдущим