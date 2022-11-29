from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    fields=['name','priority','date']
    context_object_name = 'tasks'
    ordering = ['priority']

class TaskDetailsView(DetailView):
    model=Task
    template_name = 'details.html'
    context_object_name = 'tasks'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'tasks'
    fields=['name','priority','date']

    def get_success_url(self):
        return reverse_lazy('index')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('index')

def add(request):
    if request.method=='POST':
        name=request.POST.get('name','')   # request.POST.get() will assign '<value>' (second argument) to the field if no value passed
        priority=request.POST.get('priority','')  #request.POST.get() only sets values for char or textchar
        date=request.POST.get('date')
        task=Task(name=name,priority=priority,date=date)
        task.save()
        return redirect('/')
# def index(request):
#     tasks=Task.objects.all()
#     if request.method=='POST':
#         name=request.POST.get('name','')   # request.POST.get() will assign '<value>' (second argument) to the field if no value passed
#         priority=request.POST.get('priority','')  #request.POST.get() only sets values for char or textchar
#         date=request.POST.get('date')
#         task=Task(name=name,priority=priority,date=date)
#         task.save()
#
#     return render(request,'index.html',{'tasks':tasks})

# def delete(request,task_id):
#     if request.method=='POST':
#         task=Task.objects.get(id=task_id)
#         task.delete()
#         return redirect('/')
#     return render(request,'delete.html')
#
# def update(request,id):
#     task=Task.objects.get(id=id)
#     form=TodoForm(request.POST or None, instance=task)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request,'update.html',{'form':form,'task':task})

