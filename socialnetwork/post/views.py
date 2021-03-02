from django.shortcuts import render , get_object_or_404 , redirect
from django.views.generic import ListView , DetailView , UpdateView , DeleteView , CreateView , TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post , Comment
from django.urls import reverse_lazy , reverse
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
import urllib
# Create your views here.
################################################################################
#post views
liked = False

def home(request , liked = liked):
    users = User.objects.all()
    context = {
        'home_posts': Post.objects.all().order_by('-created_date'),
        'liked':liked,
        'users':users,
    }
    return render(request , 'home.html' , context)

class PostCreateView(LoginRequiredMixin , CreateView):
    model = Post
    fields = {'title' , 'post_picture' , 'caption'}

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'profile.html'
    ordering = ['-created_date']


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self , *args , **kwargs):
        post = get_object_or_404(Post , id = self.kwargs['pk'])
        liked = False
        if post.like.filter(id = self.request.user.id).exists():
            liked = True
        else:
            liked = False
        context = super(PostDetailView , self).get_context_data()
        context['total_likes'] = post.total_likes()
        context['liked'] = liked
        return context

class PostUpdateView(UpdateView):
    model = Post
    fields = {'title' , 'caption'}

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')

################################################################################
#comment views
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        form.instance.userr = request.user
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'post/comment_form.html', {'form': form})


class CommentListView(ListView):
    model = Comment
    context_object_name = 'comments'
    template_name = 'post/post_detail.html'

class CommentDeleteView(DeleteView):
    model = Comment
    def get_success_url(self , **kwargs):
        post = self.post
        return reverse_lazy('home')

def reply_comment(request , pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        form.instance.userr = request.user
        form.instance.parent = comment
        post = comment.post
        if form.is_valid():
            reply_comment = form.save(commit=False)
            reply_comment.post = post
            reply_comment.save()
            return redirect('post:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'post/comment_form.html', {'form': form})


################################################################################
def add_like_to_post_detail(request , pk):
    post = get_object_or_404(Post , id = request.POST.get('like'))
    if post.like.filter(id = request.user.id).exists():
        post.like.remove(request.user)
        liked = False
    else:
        post.like.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post:post_detail' , kwargs = {'pk':pk}))

class LikeListView(ListView):
    model = Post
    template_name = 'post/like_list.html'
    context_object_name = 'posts'
