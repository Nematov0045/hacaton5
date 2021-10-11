from django.shortcuts import render
from ..models import Market
def homepage(request):
    return render(request,'card.html',{'posts':Market.objects.all()})