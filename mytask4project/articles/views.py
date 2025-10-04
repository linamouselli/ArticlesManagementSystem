from urllib import request

from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from .forms import ArticleForm

from .models import Article

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'article_list.html', {'articles': articles})

class ArticleCreateView(FormView):
    form_class = ArticleForm
    template_name = 'article_form.html'
    context_object_name = 'article'
    success_url = 'article_list'

    def form_valid(self, form):
        title = form.cleaned_data['title']
        content = form.cleaned_data['content']
        Article.objects.create(title=title, content=content)
        return redirect(self.success_url)
    def form_invalid(self, form):
        print("Something went wrong, please try again")
        print(form.errors)
        return super().form_invalid(form)