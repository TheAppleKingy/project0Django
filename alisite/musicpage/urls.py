from django.urls import path
from musicpage import views


urlpatterns=[
    path('music/',views.music,name='music'),
]