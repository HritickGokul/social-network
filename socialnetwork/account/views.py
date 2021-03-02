from django.shortcuts import render , redirect
from django.views.generic import TemplateView , CreateView , ListView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy , reverse
from . import forms
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from post.models import Post
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('home')
    template_name = 'account/signup.html'

class Suggestion(ListView):
    model = User
    context_object_name = 'userss'
    template_name = 'account/user_list.html'

count = 0
@login_required
def profile(request , slugg , count = count):
    obj = Profile.objects.get(slug = slugg)
    posts = Post.objects.all()
    followed = False
    for post in posts:
        if post.author == obj.user:
            count = count + 1
    if obj.followers.filter(id = request.user.id).exists():
        followed = False
    else:
        followed = True
    context = {'count':count , 'posts':Post.objects.all().order_by('-created_date') , 'obj':obj , 'followed':followed}
    return render(request, 'account/profile.html' , context)

@login_required
def profile_edit(request , slugg):
    if request.method == 'POST':
        u_form = forms.UserForm(request.POST, instance=request.user)
        p_form = forms.ProfileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('home')

    else:
        u_form = forms.UserForm(instance=request.user)
        p_form = forms.ProfileForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request , 'account/profile_update.html' , context)

def add_follower(request , slugg):
    prof = Profile.objects.get(slug = slugg)
    followed = False
    if prof.followers.filter(id = request.user.id).exists():
        prof.followers.remove(request.user)
        followed = False
        request.user.profile.following.remove(prof.user)
    else:
        prof.followers.add(request.user)
        followed = True
        request.user.profile.following.add(prof.user)
    return HttpResponseRedirect(reverse('account:profile' , kwargs = {'slugg':slugg}))

@csrf_exempt
def search_user(request):
    users = User.objects.all()
    if request.method == 'POST':
        user_name = request.POST.get('search_user_name')
        for user in users:
            if user.username == user_name:
                context = {'search_user_name':user}
                break
            else:
                context = {'search_user_name':None}
                continue
        return render(request , 'account/search.html' , context)
