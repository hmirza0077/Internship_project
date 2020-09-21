from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.db.models import F
from django.utils.timezone import now, timedelta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def product_list(request, category_slug=None, size=None):

    products = Product.available.all()
    number_of_products = len(products)
    
    
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    page = request.GET.get('page', 1)
    paginator = Paginator(products, 3)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {'category': category, 'categories': categories, 'products': products, 'now': now(), 'timedelta': timedelta(days=1), 'number_of_products': number_of_products}
    return render(request, 'shop/list.html', context=context)

def product_detail(request, id, slug):
    
    product = get_object_or_404(Product, id=id, slug=slug, is_available=True)
    # Everytime user click on a product add 1 to visit_num using F() object and show in list of product page.
    product.visit_num = F('visit_num') + 1
    product.save()
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'cart_product_form': cart_product_form, 'now': now(), 'timedelta': timedelta(days=1)}
    return render(request, 'shop/detail.html', context=context)
