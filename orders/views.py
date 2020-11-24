from django.shortcuts import redirect, render
from .tasks import order_created
from .models import OrderItem, Order
from .forms import OrderForm
from cart.cart import Cart
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from coupons.forms import CouponApplyForm
import weasyprint
from coupons.models import Coupon

def order_create(request):

    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
                coupon = Coupon.objects.get(id=cart.coupon_id)
                coupon.active = False
                coupon.save()
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                        price=item['price'], quantity=item['quantity'])
            
            # clear the cart
            cart.clear()
            # launch asynchronous task in celery: Send email
            #order_created.delay(order.id)
            # return render(request, 'orders/created.html', {'order': order})
            request.session["order_id"] = order.id
            return redirect('payment:request')
    
    form = OrderForm()
    context = {'cart': cart, 'form': form}
    return render(request, 'orders/checkout.html', context=context)


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})

@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('admin/orders/order/pdf.html', {'order':order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f"filename=Order {order.id}.pdf"
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + '/details/assets/css/pdf.css')])
    return response