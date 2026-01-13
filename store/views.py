from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Cart, CartItem
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/home.html', context)

@login_required
def add_to_cart(request, product_id):
    cart = request.session.get('cart',[])
    cart.append(product_id)
    request.session['cart']=cart
    return redirect('cart_view')
@login_required
def cart_view(request):
    cart = request.session.get('cart',[])
    products = Product.objects.filter(id__in=cart)
    return render(request,'store/cart.html',{'products':products})
