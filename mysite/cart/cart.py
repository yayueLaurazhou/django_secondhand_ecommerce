from mainPage.models import Product
from django.contrib import messages


class Cart():
	def __init__(self, request):
		self.session = request.session
		cart = self.session.get('session_key')

		if 'session_key' not in request.session:
			cart = self.session['session_key'] = {}

		self.cart = cart

	def add(self, product):
		product_id = str(product.id)
		if product_id in self.cart:
			pass
		else:
			self.cart[product_id] = {'price': str(product.price)}
		self.session.modified = True
	
	def delete(self, product):
		product_id = str(product)
		if product_id in self.cart:
			del self.cart[product_id]

		self.session.modified = True
		

	def cart_total(self):
		product_ids = self.cart.keys()
		products = Product.objects.filter(id__in=product_ids)
		total = 0
		
		for key, value in self.cart.items():
			key = int(key)
			for product in products:
				if product.id == key:
						total = total + product.price
		return total

	def __len__(self):
		return len(self.cart)
	
	def get_prods(self):
		product_ids = self.cart.keys()
		products = Product.objects.filter(id__in=product_ids)
		return products

	