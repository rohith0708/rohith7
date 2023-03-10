from django.urls import path,include
from. import views


app_name='cart'

urlpatterns = [
    path('add/<int:Product_id>/',views.add_cart,name='add_cart'),
    path('',views.cart_detail,name='cart_detail'),
    path('remove/<int:Product_id>/',views.cart_remove,name='cart_remove'),
    path('full_remove/<int:Product_id>/', views.cart_delete, name='cart_delete')

]