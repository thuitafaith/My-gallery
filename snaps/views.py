from django.shortcuts import render
from .models import Image,Location,Category
# Create your views here.
def intro(request):
    images = Image.objects.all()

    return render(request, 'intro.html',{'images':images})
