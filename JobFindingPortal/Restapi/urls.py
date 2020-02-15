from django.urls import path, include 
from . import views

urlpatterns = [
    path('job/page/<int:page>/size/<int:size>', views.getJobs,name='get'),
    path('job/', views.addJobs,name='post'),
    path('job/<int:id>', views.deleteJobs,name='delete'),
    path('updatejob/<int:id>', views.updateJobs,name='put'),
]