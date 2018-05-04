from django.shortcuts import render
from .models import Image,Location,Category
# Create your views here.
def intro(request):
    return render(request, 'intro.html')
