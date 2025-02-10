from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm


def home(request):
    # return HttpResponse('Hello, World!')
    return render(request, 'webapp/index.html')


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'webapp/register.html', context)