from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from .forms import work
def define(request):
    if request.method=='POST':
        form=work(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        
    else:
        form=work()

    return render(request,'main.html',{'form':form})

from .models import mydetails
def myproject(request):
    mdet=mydetails.objects.all()
    return render(request,'rendering.html',{'mdet':mdet})

def editform(request,pk):
    edit=get_object_or_404(mydetails, pk=pk)
    if request.method=='POST':
        form=work(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('myproject')
    else:
        form=work(instance=edit)
    return render(request, 'edit_form.html',{'form':form,'edit':edit})

def deleteform(request,pk):
    edit=get_object_or_404(mydetails, pk=pk)
    if request.method=='POST':
        edit.delete()
        return redirect('myproject')
    return render(request, 'delete_form.html',{'edit':edit})

