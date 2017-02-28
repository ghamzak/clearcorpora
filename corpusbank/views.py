from django.shortcuts import render, get_object_or_404
from .models import Corpusobject

# Create your views here.
def post_list(request):
    posts = Corpusobject.objects.filter(knownloc = True).order_by('catid')
    return render(request, 'corpusbank/post_list.html', {'posts' : posts})

def post_detail(request, pk):
	post = get_object_or_404(Corpusobject, pk=pk)
	return render(request, 'corpusbank/post_detail.html', {'post': post})
