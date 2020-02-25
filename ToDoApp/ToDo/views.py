from django.shortcuts import render,redirect
from django.utils import timezone
from .models import *

# Create your views here.
def home(request):
    all_todo=Todo.objects.all().order_by("added_date")
    params={'todo_item':all_todo}
    return render(request, 'main/index.html',params)

def todo(request):
    if request.method=="POST":
        content=request.POST['content']
        date_time=timezone.now()
        todo=Todo(text=content,added_date=date_time)
        print(todo)
        todo.save()
        return redirect('home')
    else:
        render(request,'main/index.html')

def update_task(request,slug):
    Todo.objects.filter(id=slug).update(status='primary')
    
    return redirect('home')


def delete_task(request,slug):
    Todo.objects.filter(id=slug).delete()
    
    return redirect('home')
    