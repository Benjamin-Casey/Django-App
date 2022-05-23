from atexit import register
from django.urls import path

from . import views

urlpatterns = [
    # /sleep/
    path('', views.index, name = 'index'),

    # /sleep/user/1/
    path('user/<int:user_id>/', views.user_info, name='user_info'),

    # /sleep/group/Fans Assembly/
    # path('group/<int:group_id>/', views.group_info, name='group_info'),
    path('group/<str:group_name>/', views.group_info, name='group_info'),

    # /sleep/group/Fans Assembly/1  
    path('group/<str:group_name>/<int:alarm_id>', views.alarm_info, name='alarm_info'),
]
