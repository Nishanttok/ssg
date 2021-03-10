from django.urls import path
from . import views

urlpatterns = [
    path('', views.hp, name="hp"),
    path('cpage',views.cpage, name="cpage")    

]
