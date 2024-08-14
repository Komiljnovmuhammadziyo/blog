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

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Islam, Comment
from .forms import CommentForm


class IslamDetailView(View):
    def get(self, request, id):
        islam = get_object_or_404(Islam, id=id)
        comments = Comment.objects.all()  # Bu islam obyektiga bog'langan barcha izohlarni olish
        comment_form = CommentForm()

        context = {
            'islam': islam,
            'comments': comments,
            'comment_form': comment_form
        }

        return render(request, 'islam/islam_detail.html', context)

    def post(self, request, id):
        islam = get_object_or_404(Islam, id=id)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.islam = islam
            comment.user = request.user
            comment.save()
            return redirect('blog:islam-view', id=id)  # Izoh qo'shilgandan keyin shu betga qayta yo'naltirish

        comments = islam.comments.all()
        context = {
            'islam': islam,
            'comments': comments,
            'comment_form': comment_form
        }

        return render(request, 'islam/islam_detail.html', context)


class IslamListView(View):
    def get(self, request):
        islam = Islam.objects.filter(status='published')
        context = {
            'islam': islam,
        }
        return render(request, 'islam/islam_list.html', context)
# Izoh qo'shish

from django.shortcuts import render, redirect
from django.views import View
from .models import Islam, Comment
from .forms import CommentForm

class AddCommentView(View):
    def get(self, request, pk):
        # Faqat 'GET' metodida forma ko'rsatish mumkin
        form = CommentForm()
        return render(request, 'islam/islam_detail.html', {'form': form})

    def post(self, request, pk):
        # 'POST' metodida commentni saqlash
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.islam = Islam.objects.get(pk=pk)
            comment.save()
            return redirect('blog:islam-list-view')  # Yangi comment qo'shilgandan keyin qayerga yo'naltiriladi
        return render(request, 'islam/islam_detail.html', {'form': form})


class EditCommentView(View):
    def get(self, request, id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        islam = comment.islam
        comments = Comment.objects.filter(islam=islam).exclude(id=comment_id)
        if comment.user != request.user:
            messages.error(request, "You do not have permission to edit this review.")
            return redirect(reverse('islam:islam-view', kwargs={'id': id}))

        comment_form = CommentForm(instance=comment)
        return render(request, 'crud/edit.html', {'form': comment_form, 'islam': islam, 'comments': comments})

    def post(self, request, id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)

        # Check if the user is authorized to edit the comment
        if comment.user != request.user:
            messages.error(request, "You do not have permission to edit this review.")
            return redirect(reverse('islam:islam_view', kwargs={'id': id}))

        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, "Review updated successfully.")
            return redirect(reverse('islam:islam-view', kwargs={'book_id': id}))
        else:
            messages.error(request, "Please correct the error below.")

        return render(request, 'crud/edit.html', {'form': comment_form})




class AddPostView(CreateView):
    model = Islam
    form_class = AddPostForm
    template_name = 'posts/add_post.html'
    success_url = reverse_lazy('blog:islam-list-view')




