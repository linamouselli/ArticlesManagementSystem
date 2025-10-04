from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.article_list, name='article_list'),
    path('articles/add/', views.ArticleCreateView.as_view(), name='new_article'),
]