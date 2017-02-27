from django.shortcuts import render
from .models import Corpusobject

# Create your views here.
def post_list(request):
    desired = Corpusobject.objects.filter(knownloc = True).order_by('catid')
    return render(request, 'corpusbank/post_list.html', {'desired' : desired})
