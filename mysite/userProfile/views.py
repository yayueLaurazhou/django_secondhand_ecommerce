from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from mainPage.models import Product
from .forms import NewItemForm, EditItemForm

@login_required
def profile(request):
    items = Product.objects.filter(created_by=request.user)
    return render(request, 'userProfile/profile.html', {'items': items})



@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('ProductDetails:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'userProfile/itemform.html', {
        'form': form,
        'title': 'Sell a new item',
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Product, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ("Item successfully edited!"))
            return HttpResponseRedirect(reverse('productDetails:detail',  kwargs={'pk': item.id}))
        else:
            print(form.errors)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'userProfile/itemform.html', {
        'form': form,
        'title': 'Edit item',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Product, pk=pk, created_by=request.user)
    item.delete()
    messages.success(request, ("Item successfully deleted!"))

    return redirect('userProfile:profile')