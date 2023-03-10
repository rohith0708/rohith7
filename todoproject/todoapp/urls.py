from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('detail',views.detail,name='detail'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('tasklist/',views.tasklist.as_view(),name='tasklist'),
    path('taskdetail/<int:pk>/',views.taskdetail.as_view(),name='taskdetail'),
    path('taskupdate/<int:pk>/',views.taskupdate.as_view(),name='taskupdate'),
    path('taskdelete/<int:pk>/',views.taskdelete.as_view(),name='taskdelete')
]