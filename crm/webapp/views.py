from django.shortcuts import render
from .forms import CreateUserForm, LoginForm

def home(request):
    # return HttpResponse('Hello, World!')
    return render(request, 'webapp/index.html')