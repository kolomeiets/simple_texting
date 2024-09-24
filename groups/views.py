from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import requests

from .models import Group, GroupUsers
from .forms import GroupForm

@login_required(login_url="/auth/login/")
def index_view(request):
    groups = Group.objects.all().order_by('-date_created')
    for g in groups:
        g.current_user_is_member = True if request.user.is_group_member(g) else False

    return render(request, "groups/list.html", { "groups": groups})


@login_required(login_url="/auth/login/")
def add_view(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            gu = GroupUsers(group_id=group.id, user_id=request.user.id)
            gu.save()

            return redirect("groups:index")
    else:
        form = GroupForm()

    return render(request, "groups/add.html", {"form":form})


@login_required(login_url="/auth/login/")
def leave_view(request, group_id):
    GroupUsers.objects.filter(group_id=group_id, user_id=request.user.id).delete()
    return redirect("groups:index")



@login_required(login_url="/auth/login/")
def join_view(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    GroupUsers.objects.create(group=group, user=request.user)
    group.send_invitation(request.user)
    return redirect("groups:index")

@login_required(login_url="/auth/login/")
def message_view(request):
    response = requests.get(
        "https://api-app2.simpletexting.com/v2/api/messages",
        headers={"Authorization": f"Bearer {settings.SIMPLE_TEXTING_API_TOKEN}", "Content-Type": "application/json"},
        #params={"q": "language:python", "sort": "stars", "order": "desc"},

    )
    #print(response.status_code)

    return JsonResponse(response.json())

@login_required(login_url="/auth/login/")
def message_send_view(request):
    json = {
        "contactPhone": "+12067396959",
        "mode": "SINGLE_SMS_STRICTLY",
        "text": "POST API MESSAGE TEXT 2"
    }
    response = requests.post(
        "https://api-app2.simpletexting.com/v2/api/messages",
        headers={"Authorization": f"Bearer {settings.SIMPLE_TEXTING_API_TOKEN}"},
        json=json
    )
    print(response.status_code)

    return JsonResponse(response.json())