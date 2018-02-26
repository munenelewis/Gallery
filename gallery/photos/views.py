from django.shortcuts import render
from .models import Image,Location,Category
from django.http import HttpResponse

# Create your views here.
def welcome(request):
  
    photos = Image.objects.all()
    arg =  { "photos": photos}

    return render(request, 'welcome.html',arg)


def photos(request,photo_id):
    try:
        photo = Image.objects.get(id = photo_id)
        print(photo.location)
    except DoesNotExist:
        raise Http404()
    return render(request,"photo.html", {"photo":photo})

def search_results(request):
    if 'photos' in request.GET and request.GET['photos']:
        search_term = request.GET.get('photos')
        searched_photo = Image.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'search.html', {"message":message, "photos":searched_photo})
    else:
        message = 'You haven\'t searched for any photos.'
        return render(request, 'search.html', {"message":message})