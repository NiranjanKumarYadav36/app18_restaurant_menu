from . import views
from django.urls import path

urlpatterns =[
    path('', views.MenuList.as_view(), name='home'), # as_view render the class
    path('menu_list_detail/<int:pk>/', views.MenuItemDetails.as_view(), name='details'),
    path('about/', views.about, name='about')
]
