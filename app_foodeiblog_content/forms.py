from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'text', 'author', 'image', 'author_email', 'author_phone', 'author_photo',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 
                                            'placeholder': 'Название рецепта',
                                            'required': 'required'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'label': 'Изображение'}),
            'author_email': forms.EmailInput(attrs={'class': 'form-control',
                                             'required': 'required'}),
            'author_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'author_photo': forms.FileInput(attrs={'class': 'form-control', 'label': 'Фото автора'}),

        }