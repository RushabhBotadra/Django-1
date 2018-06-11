from django.urls import path
from . import views

urlpatterns=[
    #/product/
    path('',views.index, name='index'),

    #/product/name/
    path('<str:Name>/',views.detail,name='detail'),
]
