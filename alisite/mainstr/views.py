from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.template.loader import render_to_string



# Create your views here.
def main(request):
    return render(request,'mainstr/mainpage.html')

def page_not_found(request,exeption):#обработка исключения(код 404)
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')


                                            
                                            
                            