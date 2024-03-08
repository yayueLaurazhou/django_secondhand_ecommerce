from mainPage.models import Product
from django.contrib import messages


class Cart():
	def __init__(self, request):
		self.session = request.session
		self.request = request
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

	def cart_total(self):
		product_ids = self.cart.keys()
		products = Product.objects.filter(id__in=product_ids)
		quantities = self.cart
		total = 0
		
		for key, value in quantities.items():
			key = int(key)
			for product in products:
				if product.id == key:
					if product.is_sale:
						total = total + (product.sale_price * value)
					else:
						total = total + (product.price * value)
		return total
	
	
	
	def get_prods(self):
		product_ids = self.cart.keys()
		products = Product.objects.filter(id__in=product_ids)
		return products


	def __len__(self):
		return len(self.cart)
	
	def get_prods(self):
		product_ids = self.cart.keys()
		products = Product.objects.filter(id__in=product_ids)
		return products

	def delete(self, product):
		product_id = str(product)
		# Delete from dictionary/cart
		if product_id in self.cart:
			del self.cart[product_id]

		self.session.modified = True

		# Deal with logged in user
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
			current_user.update(old_cart=str(carty))