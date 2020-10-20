from django import forms
from django.utils.translation import gettext_lazy as _

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
# COLOR_CHOICES = (
#         ('red', 'قرمز'),
#         ('brown', 'قهوه ای'),
#         ('yellow', 'زرد'),
#         ('black', 'مشکی'),
#         ('blue', 'آبی'),
#         ('green', 'سبز'),
#         ('pink', 'صورتی'),
#         ('gray', 'خاکستری'),
#     )

class CartAddProductForm(forms.Form):

    # color = forms.CharField(max_length=50, label=False, widget=forms.HiddenInput)
    # color = forms.TypedChoiceField(choices=COLOR_CHOICES, label=False)
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label=_('تعداد'))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)