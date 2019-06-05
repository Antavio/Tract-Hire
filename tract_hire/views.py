from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    tractors = Tractor.fetch_all_tractors()
    return render(request,'tract_hire/index.html',{"tractors":tractors})

def search_category(request):
    if 'category' in request.GET and request.GET ["category"]:
        search_term = request.GET.get("category")
        searched_tractors = Tractor.search_tractor(search_term)
        message = f'{search_term}'

        return render(request, 'search/search.html', {"message":message, "searched_tractors":searched_tractors})

    else:
        message = "No search results yet!"
        return render (request, 'search/search.html', {"message": message})

@login_required(login_url='/accounts/login/')
def tractor_details(request,tractor_id):
    try:
        single_tractor = Tractor.get_single_tractor(tractor_id)

    except Exception as  e:
        raise Http404()
    return render(request,'tract_hire/tractor_details.html',{"single_tractor":single_tractor})