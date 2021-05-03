from django.shortcuts import render, HttpResponse, redirect
from home.models import task

# Create your views here.
def home(request):
    context = {'success' : False}

    if request.method == "POST":
        # handels the form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        # this will save our database into task directory
        ins = task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success' : True}
    return render(request, 'index.html', context)
def tasks(request):
    # to fetch the tasks from the database and pass it to a task templates
    allTasks = task.objects.all()
    context = {'tasks' : allTasks}
    return render(request, 'tasks.html', context)

def delete(request, task_id):
    if request.method == 'POST':
        task.objects.get(id=task_id).delete()
        allTasks = task.objects.all()
        context = {'tasks': allTasks}
        return render (request, 'tasks.html', context)