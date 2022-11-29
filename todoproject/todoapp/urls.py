from django.urls import path

from todoapp import views


urlpatterns = [
    path('',views.TaskListView.as_view(),name='index'),
    path('add',views.add,name='add'),
    path('cbvdetails/<int:pk>/',views.TaskDetailsView.as_view(),name='cbvdetails'),
    path('cbvedit/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvedit'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete')
    # path('',views.index,name='index'),
    # path('delete/<int:task_id>/',views.delete,name='delete'),
    # path('update/<int:id>/',views.update,name='update')
]
