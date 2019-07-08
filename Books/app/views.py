from django.shortcuts import render
from .models import Publisher, Book, Author
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    Authors = Author.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(Authors, 5)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'data':data})
