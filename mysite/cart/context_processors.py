from .cart import Cart
#passing the request data into the cart session
def cart(request):
	return {'cart': Cart(request)}