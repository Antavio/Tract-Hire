from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    tractors = Tractor.fetch_all_tractors()
    return render(request,'tract_hire/index.html',{"tractors":tractors})