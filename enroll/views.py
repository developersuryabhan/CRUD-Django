from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User


#  This function Will Add New Items And Show All Items
def home(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            form = User(name=name, email=email, password=password)
            form.save()
            form = StudentRegistration()

    else:
        form = StudentRegistration()
#Show Data
    data = User.objects.all() 
    return render(request, 'enroll/home.html', {'form':form, 'all_data': data})

# This  function will Update/Edit
def update_user(request, id):
    if request.method == 'POST':
        data = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=data)
        if form.is_valid():
            form.save()
            form = StudentRegistration()

    else:
        data = User.objects.get(pk=id)
        form = StudentRegistration(instance=data)
    return render(request, 'enroll/update.html',{'form':form})





# This  function will Delete
def delete_user(request,id):
    if request.method == 'POST':
        data = User.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/')
