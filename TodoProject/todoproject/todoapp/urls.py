from . import views
from django.urls import path

urlpatterns = [
    path('', views.add, name='add'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.update, name='edit'),
    path('cbvhome/',views.TaskListView.as_view(),name='cbvhome'),
    path('cbvdetails/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetails'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvdelete'),

]
