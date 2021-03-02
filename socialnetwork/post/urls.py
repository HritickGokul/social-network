from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('new/' , views.PostCreateView.as_view() , name = 'post_create'),
    path('<int:pk>/detail/' , views.PostDetailView.as_view() , name = 'post_detail'),
    path('<int:pk>/delete/' , views.PostDeleteView.as_view() , name = 'post_delete'),
    path('<int:pk>/update/' , views.PostUpdateView.as_view() , name = 'post_update'),
    path('<int:pk>/comment/new/' , views.add_comment_to_post , name = 'comment_create'),
    path('comment/<int:pk>/remove/', views.CommentDeleteView.as_view(), name='comment_remove'),
    path('comment/<int:pk>/reply/' , views.reply_comment , name = 'reply_comment'),
    path('<int:pk>/liked' , views.add_like_to_post_detail , name = 'liked_detail'),
    path('<int:pk>/liked_by' , views.LikeListView.as_view() , name = 'liked_by')
]
