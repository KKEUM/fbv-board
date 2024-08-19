from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.lsit, name='list'),
    path('read/<int:id>/', views.read, name='read'),
    path('regist/', views.regist, name='regist'),
    path('edcit/<int:id>/', views.edit, name='edit'),
    path('remove/<int:id>/', views.remove, name='remove'),
]