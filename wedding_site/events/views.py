from django.contrib.auth.decorators import login_required, user_passes_test
# 独立的管理员活动管理界面
def event_manage(request):
    from users.views import is_event_admin
    from django.contrib.auth.decorators import login_required
    if not request.user.is_authenticated or not is_event_admin(request.user):
        from django.shortcuts import redirect
        return redirect('/users/admin_login/')
    events = Event.objects.all()
    return render(request, 'events/event_manage.html', {'events': events})
from django.shortcuts import render, get_object_or_404, redirect

from .models import Event
from .forms import EventForm
from django.contrib.auth.decorators import user_passes_test
from users.views import is_event_admin
@user_passes_test(is_event_admin, login_url='/users/admin_login/')
def admin_event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events, 'admin': True})

def event_list(request):
    events = Event.objects.all()
    admin = False
    if request.user.is_authenticated and hasattr(request.user, 'is_event_admin') and request.user.is_event_admin:
        admin = True
    return render(request, 'events/event_list.html', {'events': events, 'admin': admin})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    admin = False
    # 只要有 ?admin=1 参数且用户是管理员，则视为管理视图
    if request.GET.get('admin') == '1' and request.user.is_authenticated and hasattr(request.user, 'is_event_admin') and request.user.is_event_admin:
        admin = True
    return render(request, 'events/event_detail.html', {'event': event, 'admin': admin})

@login_required(login_url='/users/admin_login/')
def event_create(request):
    from users.views import is_event_admin
    if not is_event_admin(request.user):
        return redirect('/users/admin_login/')
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('event_manage')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form, 'admin': True})

@login_required(login_url='/users/admin_login/')
def event_update(request, pk):
    from users.views import is_event_admin
    if not is_event_admin(request.user):
        return redirect('/users/admin_login/')
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            return redirect('event_manage')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form, 'admin': True})

@login_required(login_url='/users/admin_login/')
def event_delete(request, pk):
    from users.views import is_event_admin
    if not is_event_admin(request.user):
        return redirect('/users/admin_login/')
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        event.delete()
        return redirect('event_manage')
    return render(request, 'events/event_confirm_delete.html', {'event': event, 'admin': True})