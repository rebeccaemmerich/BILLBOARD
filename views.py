

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone
from .models import Title
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    return render(request, 'billboard/page.html')

@login_required
def post_list(request):
    pl=Title.objects.all
    return render(request,'billboard/page.html', {"posts": pl})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'billboard/post_edit.html', {'form': form})

@login_required
def post_edit(request):
    return render(request, 'billboard/page.html')

@login_required
def post_detail(request):
    form = PostForm()
    return render(request, 'billboard/page.html', {'form': form})

