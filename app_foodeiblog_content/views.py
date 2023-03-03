from django.shortcuts import render
from  django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Article
from .forms import ArticleForm

# Create your views here.


class StartpageView(TemplateView):
    template_name = 'mainpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(article_permission = True)

        return context

class ArtticleListView(ListView):
    model = Article
    template_name = "article_list.html"
    context_object_name = "articles"

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_form.html'
    success_url = reverse_lazy('app_foodeiblog_content:mainpage')
    form_class = ArticleForm

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'article_form.html'
    success_url = reverse_lazy('app_foodeiblog_content:articles_list')
    form_class = ArticleForm

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_confirm_delete.html'
    success_url = reverse_lazy('app_foodeiblog_content:articles_list')
