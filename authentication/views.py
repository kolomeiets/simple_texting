from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, UserLoginForm


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

def index_view(request):

    #return redirect("authentication:success")
    return render(request, 'index.html', {})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('groups:index')
    else:
        form = UserLoginForm()
    return render(request, 'auth/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('authentication:login')