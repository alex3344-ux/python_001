from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _



class Article(models.Model):
    author = models.ForeignKey(
        verbose_name="Автор", to="auth.User", on_delete=models.CASCADE
    )
    title = models.CharField(verbose_name="Название рецепта", max_length=256)
    slug = models.SlugField(verbose_name="slug")
    text = models.TextField(verbose_name="Описание")
    ingredients = models.TextField(verbose_name="Ингредиенты", default='Ингредиенты:')
    image = models.ImageField(verbose_name="Изображение", upload_to="articles/articles/")
    created_at = models.DateTimeField(verbose_name="Создано", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Изменено", auto_now=True)

    author_birth_day = models.DateField(verbose_name='Дата рождения', auto_now_add=True)
    author_email = models.EmailField(verbose_name='e-mail')
    author_phone = models.CharField(verbose_name='Телефон', max_length=25)
    author_photo = models.ImageField(verbose_name='Фото', upload_to="articles/photo/")

    article_permission = models.BooleanField(verbose_name='Разрешение на показ', default=False)


    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self) -> str:
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(_(self.title))
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("articles:article_detail", kwargs={"pk": self.pk})
