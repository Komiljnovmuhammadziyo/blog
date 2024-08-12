from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView

from blog_app.forms import CommentForm, AddPostForm
from blog_app.models import Islam, Comment
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, ListView
from .models import Comment
from .forms import CommentForm

class IslamDetailView(View):
    def get(self, request, id):
        islam = Islam.objects.get(id=id)
        comments = Comment.objects.filter(id=id)
        comment_form = CommentForm()

        context = {
            'islam': islam,
            'comments': comments,
            'form': comment_form
        }

        return render(request, 'islam/islam_detail.html', context)




class IslamListView(View):
    def get(self, request):
        islam = Islam.objects.all()
        context = {
            'islam': islam,
        }
        return render(request, 'islam/islam_list.html', context)
# Izoh qo'shish



class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'islam/islam_detail.html'
    success_url = reverse_lazy('blog:islam-list-view')  # Yoki izohlar ro'yxatiga yo'naltiruvchi URL





class AddPostView(CreateView):
    model = Islam
    form_class = AddPostForm
    template_name = 'posts/add_post.html'
    success_url = reverse_lazy('blog:islam-list-view')





class CommentListView(ListView):
    model = Comment
    template_name = 'islam/islam_list.html'
    context_object_name = 'comments'
    ordering = ['-created_at']


class EditCommentView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'crud/edit.html'
    success_url = reverse_lazy('blog:islam-view', pk_url_kwarg = 'id')
