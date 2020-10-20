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
    #print(modeladmin) # orders.OrderAdmin
    #print(modeladmin.model) # <class 'orders.models.Order'>
    #print(modeladmin.model._meta) # orders.order
    #print(modeladmin.model._meta.get_fields()) # tuple of all fields in model orders
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={queryset[0]}.csv'
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many\
        and not field.one_to_many]

    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name) # The getattr() function returns the value of the specified attribute from the specified object.
            # print(type(value))
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
