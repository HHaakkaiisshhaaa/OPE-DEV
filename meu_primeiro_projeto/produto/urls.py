from django.urls import path, include
from .views import lista_pessoas
from .views import new_pessoas
from .views import update_pessoas
from .views import delete_pessoas

urlpatterns = [
    
    path('lista/', lista_pessoas, name= 'lista_pessoas' ),
    path('new/', new_pessoas ,name = 'new_pessoas'  ),  
    path('update/<int:id>', update_pessoas ,name = 'update_pessoas'  ),  
    path('delete/<int:id>',delete_pessoas ,name = 'delete_pessoas'),
]

