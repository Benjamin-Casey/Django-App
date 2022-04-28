from django.urls import path

from . import views

urlpatterns = [
    # /sleep/
    path('', views.index, name = 'index'),

    # /sleep/user/1/
    path('user/<int:user_id>/', views.user_info, name='user_info'),

    # /sleep/group/1/
    path('group/<int:group_id>/', views.group_info, name='group_info'),
]
