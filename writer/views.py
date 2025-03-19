from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="my-login")
def writer_dashaboard(request):
    return render(request, 'writer/writer_dashboard.html')
