from django.shortcuts import render
from .models import Image,Location,Category
from django.http import HttpResponse

# Create your views here.
def welcome(request):
  
    photos = Image.objects.all()
    arg =  { "photos": photos}

    return render(request, 'welcome.html',arg)

def search_results(request):

    if 'photos' in request.GET and request.GET['photos']:
        search_term = request.GET.get('photos')
        search_photos = Image.search_category(search_term)

        message = f"{search_term}"

        return render(request, 'search.html',{'message':message,'photos':search_photos})

    else:
        message = 'you havent searched anything'

        return render(request,'search.html',{'message':message})
