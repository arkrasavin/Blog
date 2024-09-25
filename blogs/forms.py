from django import forms

from blogs.models import Blog, BlogPost


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['blog']
        labels = {'blog': ''}


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['text_blog']
        labels = {
            'text_blog': 'Запись поста'
        }
        widgets = {
            'text_blog': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите ваш текст',
                }
            )
        }
