from django.conf.urls.static import static
from django.urls import path

from blog import settings
from blog_app.views import IslamDetailView, IslamListView, AddCommentView, EditCommentView, AddPostView

app_name = 'blog'

urlpatterns = [
    path('islam/<int:id>', IslamDetailView.as_view(), name='islam-view'),
    path('', IslamListView.as_view(), name='islam-list-view'),
    path('add-comment/<int:islam_id>', AddCommentView.as_view(), name='comment-view'),
    path('comment/<int:id>', EditCommentView.as_view(), name='edit-comment-view'),
    path('add-post/', AddPostView.as_view(), name='post-view')
    # path('umra/', HajView.as_view(), name='umra-view')
    # path('umra/', HajView.as_view(), name='umra-view')
    # path('umra/', HajView.as_view(), name='umra-view')
    ]

if settings.DEBUG:
    urlpatterns += static(settings. MEDIA_URL, document_root=settings.MEDIA_ROOT)

