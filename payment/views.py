from django.http import request
from orders.models import OrderItem
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from suds.client import Client

MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
client = Client('https://sandbox.zarinpal.com/pg/services/WebGate/wsdl')
amount = 1000 # Required
description = 'پرداخت شما با موفقیت انجام شد'
email = 'hmirza0077@yahoo.com' # Optional
mobile = '09129618407' # Optional
CallbackURL = 'http://localhost:8000/payment/verify/' #TODO: need to edit for realy server.

def send_request(request):
    order = get_object_or_404(OrderItem, order=request.session.get('order_id'))
    result = client.service.PaymentRequest(MERCHANT, order.price, description, email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://sandbox.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error Code: ' + str(result.Status))

def verify(request):
    if request.GET.get('Status') == 'OK':
        order = get_object_or_404(OrderItem, order=request.session.get('order_id'))
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], order.price)
        if result.Status == 100:
            # return HttpResponse('Transaction success. \nRefID: ' + str(result.RefID))
            return render(request, 'orders/created.html', {'order': order})
        elif result.Status == 101:
            return HttpResponse('Transaction submitted: ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user.')
