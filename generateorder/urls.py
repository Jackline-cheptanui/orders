

from django.urls import path
from.views import order_list,register_order,edit_order,delete_order
from django.conf.urls import url
from . import views


from .import views
urlpatterns=[
    path("register_order/",register_order,name='register_order'),
    path('list/', order_list,name='order_list'),
    path("edit/<int:id>/",edit_order,name="edit_order"),
    path('delete/<int:id>/',delete_order,name="delete_order"),
    

]