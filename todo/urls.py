from django.urls import path
from . import views
from django.urls import path
from .views import register_view, login_view, logout_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', views.TodoListView.as_view(), name='todo-list'),
    path('create/', views.CreateTodo.as_view(), name="create-todo"),
    path('detail/<int:pk>/', views.TodoListView.as_view(), name="detail-todo"),
    path('update/<int:pk>/', views.UpdateTodoView.as_view(), name="update-todo"),
    path('delete/<int:pk>/', views.DeleteTodoView.as_view(), name="delete-todo"),
    path('edit/<int:pk>/', views.EditTodoView.as_view(), name="edit-todo"),
   

]