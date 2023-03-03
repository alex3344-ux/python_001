from django.urls import path
from .views import StartpageView, ArtticleListView, ArticleUpdateView, ArticleCreateView, ArticleDeleteView

app_name = "app_foodeiblog_content"

urlpatterns = [
    path("", StartpageView.as_view(), name="startpage"),
    # path("", ArtticleListView.as_view(), name="startpage"),

    path("articles/", ArtticleListView.as_view(), name="article_admin_page"),

    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
]