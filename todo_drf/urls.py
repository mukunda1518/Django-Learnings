from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="todo-api-overview"),
    path("task-list/", views.taskList, name="todo-task-list"),
    path("task-detail/<str:pk>", views.taskDetail, name="todo-task-detail"),
    path("task-create/", views.taskCreate, name="todo-task-create"),
    path("task-update/<str:pk>", views.taskUpdate, name="todo-task-update"),
    path("task-delete/<str:pk>", views.taskDelete, name="todo-task-delete"),
    path('students/', views.StudentList.as_view()),
    path('students/<int:pk>', views.StudentDetails.as_view()),
]

