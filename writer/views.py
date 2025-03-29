from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm, UpdateUserForm
from .models import Article
from account.models import CustomUser

# Create your views here.
@login_required(login_url="my-login")
def writer_dashboard(request):
    return render(request, 'writer/writer-dashboard.html')


@login_required(login_url="my-login")
def create_article(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('my-articles')
    context = {'form': form}
    return render(request, 'writer/create-article.html', context)


@login_required(login_url="my-login")
def my_articles(request):
    current_user = request.user.id
    articles = Article.objects.filter(user=current_user).all()
    context = {'articles': articles}
    return render(request, 'writer/my-articles.html', context)

@login_required(login_url="my-login")
def update_article(request, pk):
    try:
        article = Article.objects.get(id=pk, user=request.user)
        form = ArticleForm(instance=article)
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('my-articles')
        context = {'form': form}
        return render(request, 'writer/update-article.html', context)
    except:
        return redirect('my-articles')
    
@login_required(login_url="my-login")
def delete_article(request, pk):
    try:
        article = Article.objects.get(id=pk, user=request.user)
        if request.method == 'POST':
            article.delete()
            return redirect('my-articles')
    except:
        return redirect('my-articles')
    return render(request, 'writer/delete-article.html')

@login_required(login_url="my-login")
def account_management(request):
    form = UpdateUserForm(instance=request.user)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('writer-dashboard') 
    context = {'form': form}
    return render(request, 'writer/account-management.html', context)

@login_required(login_url="my-login")
def delete_account(request):
    if request.method == 'POST':
        delete_user = CustomUser.objects.get(email=request.user)
        delete_user.delete()
        return redirect('my-login')
    return render(request, 'writer/delete-account.html')