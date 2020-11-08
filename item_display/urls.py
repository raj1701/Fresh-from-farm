from django.urls import path

from . import views

urlpatterns = [
    path('',views.index , name='index'),
    path('item_display/<int:id>/', views.display , name='display')
]