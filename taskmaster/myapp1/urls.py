from django.urls import path
from . import views  #  из .(из этой же директории) имортируем файлик views.py

urlpatterns = [
    path('', views.index, name='home'),  #  проверяем, если перешли на главную страничку, то обращаемся к файлу views.py и обращаемся к методу "index"
    path('about-us', views.about, name='about'),  # обрататываем url адрес about-us. Если заходим на главную страничку, вызываем функцию index, если заходим на страничку about-us, вызываем функцию about
    path('create', views.create, name='create'),  #отслеживаем страничку create
    path("delete/<int:id>/", views.delete),
]