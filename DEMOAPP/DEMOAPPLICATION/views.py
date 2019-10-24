from django.shortcuts import render
from .models import Guest
from .models import Officer
from django.http import HttpResponse


# Create your views here.
def hi(request):
    return render(request, 'DEMOAPPLICATION/hi.html', context={"Guest": Guest.objects.all})


def news(request):
    return render(request, 'DEMOAPPLICATION/news.html')


def guestform(request):
    show = Officer.objects.filter()
    return render(request, 'DEMOAPPLICATION/guestform.html', context={"Officer": Officer.objects.all})


def about(request):
    return render(request, 'DEMOAPPLICATION/about.html')

