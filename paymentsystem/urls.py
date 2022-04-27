from django.urls import path

from . import views

urlpatterns = [
    # eg: /sleep/
    path('', views.index, name = 'index'),

    # eg: /sleep/user/2/
    # path('user/<int:user_id>/', views.user_id, name='user_info'),

    # eg: /sleep/group/3/
    # path('gropu/<int:group_id>/', views.group_info, name='group_info'),
]

