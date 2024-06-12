from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import SeatAllotment

# Create your views here.
#def home(request):
#	return HttpResponse('<h1>Data Analysis of JOSAA (Joint Seat Allocation Authority) seat allotment statistics')

def home(request):
    return render(request, 'data_analysis/home.html')

def about(request):
    return render(request, 'data_analysis/about.html')

    #data = SeatAllotment.objects.all().values()
    #return JsonResponse(list(data), safe=False)
    
def inst_wise(request):
    return render(request, 'data_analysis/inst_wise.html')