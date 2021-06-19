from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.models import TodoItem

def index(requests):
    return HttpResponse('Примитивный ответ из приложения tasks')

def complete_task(requets, uid):
    print(uid)
    return HttpResponse('OK')

def delete_task(requets, uid):
    print(uid)
    return redirect('/tasks/list')

def tasks_list(requests):
    all_tasks = TodoItem.objects.all()
    return render(
        requests,
        'tasks/list.html',
        {'tasks': all_tasks}
    )