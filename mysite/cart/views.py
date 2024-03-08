from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .cart import Cart
from mainPage.models import Product

def cart_summary(request):
	cart = Cart(request)
	cart_products = cart.get_prods
	return render(request, "cart/cart.html", {'cart_prducts': cart_products})



def cart_add(request):
	cart = Cart(request)
	if request.POST.get("action") == 'post':
		product_id = int(request.POST.get('productid'))
		product = get_object_or_404(Product, id=product_id)
		cart.add(product=product)
		response = JsonResponse({'qty' : 3})
		return response
	
	


		

