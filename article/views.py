from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .forms import Article, ArticleForm
from .models import Article, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def articles(request):
    keyword = request.GET.get("keyword")
    articles = Article.objects.all()
    
    if keyword:
        articles = Article.objects.filter(title__contains = keyword, content__contains = keyword)

    return render(request, "articles.html", {"articles":articles})


def add_comment(request, id):
    article = get_object_or_404(Article, id = id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        new_comment = Comment(comment_author = comment_author, comment_content = comment_content)
        new_comment.article = article
        new_comment.save()

    return redirect(reverse("article:viewingarticle", kwargs={"id":id}))


@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }

    return render(request, "dashboard.html", context)


def viewing_article(request, id):
    # article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article, id = id)
    comments = article.comments.all()
    return render(request, "viewingarticle.html", {"article":article, "comments":comments})


@login_required(login_url="user:login")
def add_article(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()
        messages.success(request, "The article was successfully added.")
        
        return redirect("article:dashboard")

    return render(request, "addarticle.html", {"form":form})


@login_required(login_url="user:login")
def edit_article(request, id):
    article = get_object_or_404(Article, id = id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance = article)

    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()
        messages.success(request, "The article was successfully edited.")
        
        return redirect("article:dashboard")
    
    return render(request, "editarticle.html", {"form":form})


@login_required(login_url="user:login")
def delete_article(request, id):
    article = get_object_or_404(Article, id = id)
    article.delete()
    messages.warning(request, "The article was deleted.")

    return redirect("article:dashboard")

