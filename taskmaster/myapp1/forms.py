from .models import Task  # подключаем модель Task
from django.forms import ModelForm, TextInput, Textarea  #импортируем классы

#создаем функциональную форму, поэтому создадим класс
class TaskForm(ModelForm):  # называем по имени модели + Form, все наследуется от класса Model form 
    class Meta:  #можем указать доп настройки
        model = Task
        fields = ["title", "task"]  #какие полядолжны присутствовать в самой форме, название должны быть такими же, как и в файле models.py
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),            
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }
