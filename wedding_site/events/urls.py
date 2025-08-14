from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    # path('admin/', views.admin_event_list, name='admin_event_list'),
    path('events_manage/', views.event_manage, name='event_manage'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/new/', views.event_create, name='event_create'),  # 仅管理员可访问
    path('event/<int:pk>/edit/', views.event_update, name='event_edit'),  # 仅管理员可访问
    path('event/<int:pk>/delete/', views.event_delete, name='event_confirm_delete'),  # 仅管理员可访问
]