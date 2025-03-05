from django.shortcuts import render
from .forms import CreateUserForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'account/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User registered!')
    
    context = {'RegisterForm': form}
            
    return render(request, 'account/register.html', context)

def my_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username = username, password = password)
            if user is not None and user.is_writer == True:
                login(request, user)
                return HttpResponse('You are logged in as a writer!')
            if user is not None and user.is_writer == False:
                login(request, user)
                return HttpResponse('You are logged in as a reader!')
                
    context = {'LoginForm': form}
    return render(request, 'account/my-login.html', context)