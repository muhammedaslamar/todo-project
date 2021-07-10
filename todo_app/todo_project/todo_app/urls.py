
from django.urls import path
from . import views

urlpatterns = [
path('',views.task,name='task'),
path('delete/<int:id>/',views.delete,name='delete'),
path('update/<int:id>/',views.update,name='update'),
path('tv/',views.taskList.as_view(),name='tv'),
path('dv/<int:pk>/',views.detailview.as_view(),name='dv'),
path('ud/<int:pk>/',views.updateview.as_view(),name='ud'),
    path('dv/<int:pk>/',views.deleteview.as_view(),name='dv')
]
