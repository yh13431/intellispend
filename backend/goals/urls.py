from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_goal, name='create_goal'),
    path('update/<uuid:goalId>', views.update_goal, name='update_goal'),
    path('delete/<uuid:goalId>', views.delete_goal, name='delete_goal'),
    path('', views.get_all_goals, name='get_all_goals'),
    path('<uuid:goalId>', views.get_goal, name='get_goal'),
]
