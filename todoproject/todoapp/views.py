from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from.models import Task
from.forms import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.
class tasklist(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'tas'
class taskdetail(DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name = 'task'
class taskupdate(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ['name','priority','date']

    def get_success_url(self):
        return reverse_lazy('taskdetail',kwargs={'pk':self.object.id})

class  taskdelete(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('tasklist')
def home(request):
    tas=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,"home.html",{'tas':tas})
def detail(request):
    ttas=Task.objects.all()

    return render(request,"detail.html",{'ttas':ttas})
def delete(request,id):
    done= Task.objects.get(id=id)
    if request.method=='POST':
      done.delete()
      return redirect('/')
    return render(request,"delete.html")

def update(request,id):
    task=Task.objects.get(id=id)
    f=todoform(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,"edit.html",{'f':f,'task':task})


