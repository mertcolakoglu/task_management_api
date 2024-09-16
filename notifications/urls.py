from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.NotificationListCreateView.as_view(), name='notification-list-create'),
    path('notifications/<int:pk>/', views.NotificationRetrieveUpdateDestroyView.as_view(), name='notification-detail'),
    path('notifications/mark-all-read/', views.mark_all_as_read, name='mark-all-read'),
]
