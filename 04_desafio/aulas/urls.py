from django.urls import path

from aulas import views

urlpatterns = [

    path('', views.list_aulas)
]
