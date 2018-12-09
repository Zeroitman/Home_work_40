from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task


def index_view(request):
    task = Task.objects.all()
    return render(request, 'index.html', context={
        'task': task
    })


def create_view(request):
    task = Task.objects.create(
        name=request.POST.get('name')
        )
    return redirect('index')


def delete_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={
            'task': task
        })
    elif request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            task.delete()
        return redirect('index')


def update_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    if request.method == 'GET':
        return render(request, 'edit.html', context={
            'task': task
        })
    elif request.method == 'POST':
        task.name = request.POST.get('name')
        task.save()
        return redirect('index')


def do_the_task(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    task.status = bool(request.POST.get('status', True))
    task.save()
    return redirect('index')


def delete_completed_tasks(request):
    task = Task.objects.all().filter(status=True)
    if request.method == 'GET':
        return render(request, 'all_delete.html', context={
            'task': task
        })
    elif request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            task.delete()
        return redirect('index')

