from django.urls import path, include
from .views import lista_pessoas
from .views import new_pessoas


urlpatterns = [
    
    path('lista/', lista_pessoas, name= 'lista_pessoas' ),
    path('new/', new_pessoas ,name = 'new_pessoas'  ),  
   
]

