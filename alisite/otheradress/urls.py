from django.urls import path
from otheradress import views


urlpatterns=[
    path('othadr/<int:year>',views.other_adress,name='othadr'),
]