from django.shortcuts import render,get_object_or_404
from mainPage.models import Product

def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_items = Product.objects.filter(category=product.category).exclude(pk=pk)[0:3]

    return render(request, 'productDetails/detail.html', {
        'product': product,
        'related_items': related_items
    })
    