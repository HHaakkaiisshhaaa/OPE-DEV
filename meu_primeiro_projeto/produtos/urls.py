from django.urls import path, include
from .views import lista_produto
from .views import novo_produto
from .views import update_produto
from .views import delete_produto
from .views import home

urlpatterns = [
    
    path('lista/', lista_produto, name= 'lista_produto' ),
    path('novo/', novo_produto ,name = 'novo_produto'  ),  
    path('update/<int:id>', update_produto ,name = 'update_produto'  ),  
    path('delete/<int:id>',delete_produto ,name = 'delete_produto'),
    path('home/', home, name= 'home' ),
]

