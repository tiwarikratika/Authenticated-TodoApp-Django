
from django.urls import path
from .views import *
from .  import views

urlpatterns = [
    path('',views.home, name='home'),
    path('todo/', todo, name='todo'),
    path('delete_todo/<id>', delete_todo, name='delete_todo'),
    path('mark_as_complete/<id>', mark_as_complete, name='mark_as_complete'),
    path('login_page/',login_page, name="login_page"),
    path('register_page/', register_page, name="register_page"),
    path('todo/logout/', logout, name='logout')
]
