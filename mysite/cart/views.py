from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .cart import Cart
from mainPage.models import Product

def cart_summary(request):
	cart = Cart(request)
	cart_products = cart.get_prods()
	cart_totals = cart.cart_total()
	return render(request, "cart/cart.html", {'cart_products': cart_products, 'cart_totals': cart_totals})



def cart_add(request):
	cart = Cart(request)
	if request.POST.get("action") == 'post':
		product_id = int(request.POST.get('productid'))
		product = get_object_or_404(Product, id=product_id)
		cart.add(product=product)
		cart_quantity = cart.__len__()
		response = JsonResponse({'qty' : cart_quantity})
		messages.success(request, ("Item Added to Cart!"))
		return response
	
def cart_delete(request):
	cart = Cart(request)
	if request.POST.get("action") == "post":
		product_id = int(request.POST.get('productid'))
		cart.delete(product=product_id)
		cart_quantity = cart.__len__()
		response = JsonResponse({'qty' : cart_quantity})
		messages.success(request, ("Item Deleted from Cart!"))
		return response




		

