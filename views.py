

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone
from .models import Title

def index(request):
    return render(request, 'billboard/page.html')


def post_list(request):
    pl=Title.objects.all
    return render(request,'billboard/page.html', {"posts": pl})


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


def post_edit(request):
    return render(request, 'billboard/page.html')


def post_detail(request):
    form = PostForm()
    return render(request, 'billboard/page.html', {'form': form})