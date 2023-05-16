from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path('dashboard/', views.dashboard, name = "dashboard"),   
    path('addarticle/', views.add_article, name = "addarticle"),   
    path('viewingarticle/<int:id>', views.viewing_article, name = "viewingarticle"), 
    path('edit/<int:id>', views.edit_article, name = "edit"),
    path('delete/<int:id>', views.delete_article, name = "delete"),
    path('articles/', views.articles, name = "articles"),
    path('comment/<int:id>', views.add_comment, name = "comment"), 
]
