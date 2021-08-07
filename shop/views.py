from orders.models import OrderItem
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, BookmarkProduct
from cart.forms import CartAddProductForm
from django.db.models import F
from django.utils.timezone import now, timedelta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .recommender import Recommender
from .filters import ProductFilter
from django.contrib import auth

def wishlist(request, id=None):
    cart_product_form = CartAddProductForm()
    wishlist_products = list(BookmarkProduct.objects.filter(user=request.user).values('product'))
    products = [Product.objects.get(id=product.get('product')) for product in wishlist_products]
    if id:
        # get User
        user = auth.get_user(request)
        #Trying to get a bookmark from the table, or create a new one
        bookmark, created = BookmarkProduct.objects.get_or_create(user=user, product_id=id)
        # If no new bookmark has been created,
        # Then we believe that the request was to delete the bookmark
        # if not created:
        #     bookmark.delete()

    page = request.GET.get('page', 1)
    paginator = Paginator(products, 5)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'shop/wishlist.html', {'products': products, 'cart_product_form': cart_product_form,})

def remove_from_wishlist(request, id=None):
    print('remove')
    user = auth.get_user(request)
    bookmark = BookmarkProduct.objects.get(user=user, product_id=id)
    print(bookmark)
    bookmark.delete()
    return redirect('shop:wishlist')

def product_list(request, category_slug=None, gender=None):


    language = request.LANGUAGE_CODE
    products = Product.objects.filter(is_available=True)
    number_of_products = len(products)

    gender = None
    if gender:
        products = products.filter(gender=gender) 

    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, 
                                    translations__slug=category_slug,
                                    translations__language_code=language)
        products = products.filter(category=category)

    # Filtering with django-filters
    filters = ProductFilter(request.GET, queryset=products)

    page = request.GET.get('page', 1)
    paginator = Paginator(filters.qs, 3)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {'category': category, 'categories': categories, 'products': products, 'now': now(),
                'timedelta': timedelta(days=1), 'number_of_products': number_of_products, 
                'template_name': 'shop/star_rate.html', 'filter': filters,}
    return render(request, 'shop/list.html', context=context)

def product_detail(request, id, slug, color=None):

    language = request.LANGUAGE_CODE
    products = Product.objects.filter(is_available=True) # Related products in detail page
    product = get_object_or_404(Product, id=id,
                                translations__language_code=language, 
                                translations__slug=slug,
                                is_available=True)

    is_there_any_order_with_this_product = OrderItem.objects.filter(product=product, order__first_name=request.user.first_name).exists()

    # The code below get next and previous object
    # and if the object does not exist, set it to None.
    try:
        next_product_id = product.id + 1
        next_product = get_object_or_404(Product ,id=next_product_id)
    except:
        next_product = None
    try:
        previouse_product_id = product.id - 1
        previous_product = get_object_or_404(Product ,id=previouse_product_id)
    except:
        previous_product = None

    # Everytime user click on a product add 1 to visit_num using F() object and show in list of product page.
    product.visit_num = F('visit_num') + 1
    product.save()
    cart_product_form = CartAddProductForm()

    # Recommendation System with Redis
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 6)
    print(recommended_products)

    context = {'product': product, 'cart_product_form': cart_product_form, 'now': now(), 'template_name': 'shop/star_rate.html', 'is_there_any_order':is_there_any_order_with_this_product,
                'timedelta': timedelta(days=1), 'products': products, 'next_product': next_product,
                'previous_product': previous_product, 'recommended_products': recommended_products,
                'share_telegram': {'url': product.get_absolute_url, 'text': product.name, 'link_text': "<i title='Telegram' class='fa fa-telegram mr-3' style='font-size:24px;color:#2196F3;'></i>" },
                'share_whatsapp': {'url': product.get_absolute_url, 'text': "<i title='Whatsapp' class='fab fa fa-whatsapp mr-3' style='font-size:24px;color:#1bd741;'></i>" },
                'share_linkedin': {'url': product.get_absolute_url},
                }
    return render(request, 'shop/detail.html', context=context)
