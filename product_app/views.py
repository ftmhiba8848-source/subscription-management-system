from django.shortcuts import render, redirect, get_object_or_404
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_app/product_list.html', {
        'products': products
    })


def add_product(request):
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            product_type=request.POST.get('product_type'),
            sales_price=request.POST.get('sales_price'),
            cost_price=request.POST.get('cost_price'),
            is_active=request.POST.get('is_active') == 'on'
        )
        return redirect('product_list')

    return render(request, 'product_app/add_product.html')


def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.product_type = request.POST.get('product_type')
        product.sales_price = request.POST.get('sales_price')
        product.cost_price = request.POST.get('cost_price')
        product.is_active = request.POST.get('is_active') == 'on'
        product.save()

        return redirect('product_list')

    return render(request, 'product_app/edit_product.html', {
        'product': product
    })


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(request, 'product_app/delete_product.html', {
        'product': product
    })