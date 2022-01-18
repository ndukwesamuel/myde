from django.shortcuts import render,redirect 

# Create your views here.

from Home.models import TodoData
from Home.forms import TodoForm


def home(request):
    todos = TodoData.objects.all()
    context ={
        'todolist':todos
    }

    return render( request, 'index.html', context)

def todo_detail(request, id):

    todo = TodoData.objects.get(id=id)

    context = {
        'todo':todo
    }

    return render(request, 'detail.html', context)




def todo_create(request):
    form  = TodoForm(request.POST or None)
    if form.is_valid():
        print(form)
        form.save()
        return redirect('/')
    else:
        print('bad')

    context = {
        'form': form
    }
    

    return render(request, 'create.html', context)



def todo_update(request,  id):
    todo = TodoData.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')

    context = {
        'form':form
    }


    return render(request, 'create.html', context )
