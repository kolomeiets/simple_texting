from django.shortcuts import render, redirect

# Create your views here.
from .models import Group
from .forms import GroupForm

def index_view(request):
    groups = Group.objects.all().order_by('-date_created')
    return render(request, "groups/list.html", { "groups": groups})



def add_view(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("groups:index")
    else:
        form = GroupForm()

    return render(request, "groups/add.html", {"form":form})