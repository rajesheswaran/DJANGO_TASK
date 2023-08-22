from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('competition_list',views.competition_list,name='competion-list'),
]