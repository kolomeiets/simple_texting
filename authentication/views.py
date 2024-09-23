from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreationForm


# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("authentication:success")
    else:
        form = UserCreationForm()
    return render(request, "auth/register.html", { "form": form })


def success_view(request):
    html = "<html><body>Success</body></html>"
    return HttpResponse(html)

def s_view(request):
    return redirect("authentication:success")