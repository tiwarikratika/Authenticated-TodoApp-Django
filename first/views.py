from typing import ContextManager
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    context = {'page': "homepage"}
    return render(request,'home.html',context)


# def about(request):
#     context = {'page': "aboutpage"}
#     return render(request,'about.html',context)


# def contact(request):
#     contact_obj = Contact.objects.all()
#     context = {'page': "contactpage",'contacts':contact_obj}
#     return render(request,'contact.html',context)


@login_required(login_url='/login_page/')
def todo(request):
    print(request.user)
    if request.method=="POST":
            todo = request.POST.get('todo')
            if todo is not None:
              todo_obj = Todo(todo_name = todo, user = request.user)
              todo_obj.save()
            return redirect('/todo')
    todos = Todo.objects.filter(user = request.user)
    context =  {'todos':todos}

    return render(request,'todo.html',context)


def delete_todo(request, id):
    try:
        todo = Todo.objects.get(id = id)
        todo.delete()
    except Todo.DoesNotExist:
        pass
    return redirect('/todo/')


def mark_as_complete(request,id):
    try:
        todo = Todo.objects.get(id = id)
        todo.is_complete = True
        todo.save()
    except Todo.DoesNotExist:
        pass
    return redirect('/todo/')


def register_page(request):
    if request.method=='POST':
        first_name = request.POST.get("first_name", "default value")
        last_name = request.POST.get('last_name')
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'USername Taken')
                return redirect('register_page')
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email taken")
                return redirect('register_page')
            else:
                user = User.objects.create_user(username = username, password = password1, email = email, first_name = first_name, last_name = last_name)
                user.save()
                print("User created")
                return redirect('login_page')
        else:
            print("Password doesn't match")
            return redirect('register_page')

       
        
        return redirect('/login_page/')

    else:
        return render(request,'register.html')



def login_page(request):
    if request.method =='POST':
        username = request.POST.get('username',"default value")
        password = request.POST.get('password',"default value")

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect("/todo/")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('/login_page/')


    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/home')
