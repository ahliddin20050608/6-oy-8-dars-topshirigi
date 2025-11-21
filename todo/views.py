from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from .models import Todo
from django.core.paginator import Paginator

from django.contrib.auth import get_user_model
User = get_user_model()

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu username mavjud")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        messages.success(request, "Muvaffaqiyatli roʻyxatdan oʻtdingiz!")
        return redirect("login")

    return render(request, "register.html")
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("/") 
        else:
            messages.error(request, "Login yoki parol xato!")
            return redirect("login")
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

class TodoListView(View):
    def get(self, request, pk=None):
        if pk:
            todos = get_object_or_404(Todo, pk=pk)
            return render(request, 'detail.html',{"todos":todos})
        todos = Todo.objects.all()
        paginator = Paginator(todos, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        
        
        if not todos.exists():
            return render(request, 'no-task.html')
        data = {
            'page_obj':page_obj,
            "todos":todos
        }
        return render(request, 'index.html', context=data)
    
    def post(self, request):
        return render(request,'index.html')
    
class CreateTodo(View):
    def get(self, request):
        return render(request, 'create.html')
    def post(self, request):
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        if title:
            
            Todo.objects.create(
                title = title,
                desc = desc
            )
        else:
            print("title yoq")
        return redirect('todo-list')

class UpdateTodoView(View):
    def get(self, request, pk=None):
        todos = get_object_or_404(Todo, pk=pk)
        return render(request, 'update.html', {"todos":todos})
    
    def post(self, request, pk=None):
        todos = get_object_or_404(Todo, pk=pk)
        todos.title = request.POST.get('title')
        todos.desc = request.POST.get('desc')
        todos.save()
        
        return redirect('todo-list')

class EditTodoView(View):
    def get(self, request, pk=None):
        todo = Todo.objects.get(pk=pk)       
        return render(request, 'edit.html', {"todo":todo})
    
    def post(self, request, pk=None):
        todo = Todo.objects.get(pk=pk)
        todo.title = request.POST.get("title")
        todo.desc = request.POST.get('desc')
        todo.save()
        return redirect('todo-list')


class DeleteTodoView(View):
    def get(self, request, pk=None):
        todo = get_object_or_404(Todo, pk=pk)
        return render(request, 'delete.html', {"todo":todo})
    
    def post(self, request, pk=None):
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        return redirect('todo-list')