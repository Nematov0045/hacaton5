from django.shortcuts import render
from .models import Market
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
# Create your views here.
def homepage(request):
    return render(request,'index.html',{'posts':Market.objects.all()})
def cart(request):
    return render(request,'shopingcart.html',{'posts':Market.objects.all()})
def cart2(request):
    return render(request,'shopdetails.html',{'posts':Market.objects.all()})
def contact(request):
    return render(request,'contact.html',{'posts':Market.objects.all()})
def addToCart(request,pk):
    cart_session = request.session.get('cart_session',[])
    cart_session.append(pk)
    request.session['cart_session']= cart_session
    return redirect('cart')
def create(request):
    if request.method == 'POST':
        todo = Market()
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
    return HttpResponseRedirect('/')