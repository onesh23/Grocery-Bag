from django.urls import path
from bag.views import add_Item, delete_item, index, update_Item

urlpatterns = [
    path('', index, name='index'),
    path('add_item',add_Item,name='add_item'),
    path('update_item/<int:id>',update_Item,name='update_item'),
    path('delete_item/<int:id>',delete_item,name='delete_item'),

]
