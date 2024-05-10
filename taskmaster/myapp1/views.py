from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseNotFound  #  чтобы выводить текст, подключаем библиотеку
from .models import Task  # вытаскиваем все из модели Task: то, с чем будем работать. '.' из этой же директории
from .forms import TaskForm



def index(request):  #создаем метод index
    tasks = Task.objects.all()  # получаем все обьекты из модели Task(tasks - список)
    return render(request, 'myapp1/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})  # с помощью render можем указать, какой html шаблон будет подключен, в кавычках будет шаблон страницы

def about(request):
    return render(request, 'myapp1/about-us.html')  # выводит определенный html текст на страничку

def create(request):
    error = ''
    if request.method == 'POST':  # проверяем передачу данных, посредством метода post
        form = TaskForm(request.POST)  # принимаем и сохраняем данные, которые получили от пользователя
        if form.is_valid:  # если данные, полученные от пользователя корректны, то обращаемся к форме и методу save
            form.save()
            return redirect('/')  # переадрессовываем пользователя на страницу home
        else:
            error = 'Форма некорректна'

    form = TaskForm()
    content = {
        'form': form,
        'error': error
    }
    return render(request, 'myapp1/create.html', content)


def delete(request, id):
    try:
        person = Task.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Task not found</h2>")