from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse


# def register(request: HttpRequest) -> HttpResponse:
#     if request.method != 'POST':
#         form = UserCreationForm()
#     else:
#         form = UserCreationForm(data=request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             new_user = authenticate(username=username, password=password)
#             if new_user is None:
#                 login(request, new_user)
#                 return redirect('blogs:index')
#     context = {'form': form}
#     return render(request, 'registration/register.html', context)


def register(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('blogs:index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('blogs:index')
