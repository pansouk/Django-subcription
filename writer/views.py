from django.shortcuts import render

# Create your views here.
def writer_dashaboard(request):
    return render(request, 'writer/writer_dashboard.html')