from django import forms
from django.forms import ModelForm
from blog_app.models import Comment, Islam


from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'questions')

class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'questions']

class AddPostForm(ModelForm):
    class Meta:
        model = Islam
        fields = ['name','body', 'image']

