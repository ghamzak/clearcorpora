from django.shortcuts import render, get_object_or_404, redirect
from .models import Corpusobject
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Corpusobject.objects.filter(knownloc = True).order_by('catid')
    return render(request, 'corpusbank/post_list.html', {'posts' : posts})

def post_detail(request, pk):
	post = get_object_or_404(Corpusobject, pk=pk)
	return render(request, 'corpusbank/post_detail.html', {'post': post})

# def post_new(request):
#     form = PostForm()
#     return render(request, 'corpusbank/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'corpusbank/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Corpusobject, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'corpusbank/post_edit.html', {'form': form})



