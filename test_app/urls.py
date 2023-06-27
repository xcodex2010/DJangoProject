from django.urls import path

from . import views


urlpatterns = [
    path('products/', views.products, name='products'),
    path('create-product/', views.create_product, name='creation'),
    path('create-product/create', views.create, name='create'),
    path('main/', views.main , name = 'main'),  
    path('show/', views.show_goods, name='show'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit/update', views.update, name='update'),
]