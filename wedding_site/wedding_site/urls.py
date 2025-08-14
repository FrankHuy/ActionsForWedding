from django.contrib import admin
from django.urls import path, include

from events.views import event_manage
urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('users/', include('users.urls')),
    path('events_manage/', event_manage, name='event_manage'),
]