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
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        searched_categories = Image.search_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, '    search.html', {"message": message})

