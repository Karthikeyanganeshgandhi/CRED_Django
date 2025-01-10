from django.urls import path
from .import views

urlpatterns=[
    path('define/',views.define,name='define'),
    path('myproject/',views.myproject,name='myproject'),
    path('edit/<int:pk>/',views.editform,name='editform'),
    path('delete/<int:pk>/',views.deleteform,name='deleteform'),
]