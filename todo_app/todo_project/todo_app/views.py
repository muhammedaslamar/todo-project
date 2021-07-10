from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Task
from .forms import TodoForms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy




class taskList(ListView):
    model = Task
    template_name = 'task.html'
    context_object_name = 'obj'

class detailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'





def task(request):
    obj=Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date= request.POST.get('date')
        a = Task(name=name, priority=priority,tdate=date)
        a.save()
        print('record is saved!!')
    else:
        print("error")
    return render(request,'task.html',{'obj':obj})




def delete(request,id):
    obj = Task.objects.get(id=id)
    if request.method=='POST':
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')

class deleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('tv')




def update(request,id):
    task=Task.objects.get(id=id)
    form=TodoForms(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        print("edit is doen")
        return redirect('/')

    return render(request,'update.html',{'task':task,'form':form})

class updateview(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name','priority','tdate')
    def get_success_url(self):
        return reverse_lazy('dv',kwargs={'pk':self.object.id})

