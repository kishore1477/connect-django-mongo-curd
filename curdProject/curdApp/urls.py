
from django.urls import include, path

from . import views
urlpatterns = [
    
    path('', views.index, name = "index"),
    path('contact/', views.contact, name = "contact"),
    path('addToDo/', views.addToDo, name = "addToDo"),
]
