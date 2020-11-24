from os import write
from shop.models import Product
from django.contrib import admin
from .models import Order, OrderItem
from django.urls import reverse
from django.utils.safestring import mark_safe
import csv
import datetime
from django.http import HttpResponse

def order_detail(order):
    return mark_safe('<a href="{}">View</a>'.format(reverse('orders:admin_order_detail', args=[order.id])))

def order_pdf(order):
    return mark_safe('<a href="{}">PDF</a>'.format(reverse('orders:admin_order_pdf', args=[order.id])))
order_pdf.short_description = 'Invoice'

def export_to_csv(modeladmin, request, queryset):
    # print(modeladmin) # orders.OrderAdmin
    # print(modeladmin.model) # <class 'orders.models.Order'>
    # print(modeladmin.model._meta) # orders.order
    # print(modeladmin.model._meta.get_fields()) # tuple of all fields in model orders
    # ids = [ id[0] for id in list(queryset.values_list('id')) ]    # Get the ids
    order_items = OrderItem._meta
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={queryset[0]}.csv'
    writer = csv.writer(response)

    order_fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    headers = [field.verbose_name for field in order_fields]
    headers.append('توضیحات')
    index = headers.index('coupon')
    headers.pop(index)
    headers.insert(index, 'کوپن')
    order_fields.append('توضیحات')

    # Write headers
    writer.writerow([field for field in headers])

    # Write data rows
    for obj in queryset:
        data_row = []
        order_items = OrderItem.objects.filter(order=obj.id).values('product', 'price', 'quantity')
        s = str()
        for order_item in order_items:
            price = order_item.get('price')
            quantity = order_item.get('quantity')
            product_name = Product.objects.filter(id=order_item.get('product')).values('translations__name')[1].get('translations__name')
            s += ', '.join([product_name, str(int(price)), str(quantity), 'عدد', '\n'])
        for field in order_fields:
            if field == 'توضیحات':
                data_row.append(s)
            else:
                value = getattr(obj, field.name) # The getattr() function returns the value of the specified attribute from the specified object.
                if value is None:
                    value = '-'
                if value is True:
                    value = 'پرداخت شده'
                elif value is False:
                    value = 'پراخت نشده'
                if isinstance(value, datetime.datetime):
                    value = value.strftime('%d/%m/%Y') # The strftime() function is used to convert date and time objects to their string representation
                data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name',
                    'email', 'address', 'postal_code', 'city',
                    'paid', 'created', 'updated', order_detail, order_pdf,]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [export_to_csv]
