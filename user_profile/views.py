from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, UserForm
from .models import UserProfile
from django.contrib import messages
from django.shortcuts import redirect



@login_required
def profile_detail_view(request):
    return render(request, 'user_profile/dashboard.html')

# @login_required
# def address_sidebar(request):
#     return render(request, 'user_profile/address_sidebar.html')

# @login_required
# def edit_address(request):
#     if request.method == 'POST':
#         address_form = AddressForm(request.POST or None, instance=request.user.userprofile)
#         if address_form.is_valid():
#             address_form.save()
#             return redirect('user_profile:profile_detail_view')
#     else:
#         address_form = AddressForm(instance=request.user.userprofile)
#         return render(request, 'user_profile/edit_address.html', {'address_form': address_form})
    

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_profile = UserProfileForm(request.POST, instance=request.user.userprofile)
        user_form = UserForm(request.POST, instance=request.user)
        if user_profile.is_valid() and user_form.is_valid():
            user_profile.save()
            user_form.save()
            message = messages.success(request, 'پروفایل شما با موفقیت آپدیت شد')
            return redirect('user_profile:profile_detail_view')
        else:
            message = messages.error(request, 'لطفا تمامی فیلد ها را پر کنید')
            return redirect('user_profile:edit_profile')
    else:
        user_profile = UserProfileForm(instance=request.user.userprofile)
        user_form = UserForm(instance=request.user)
    return render(request, 'user_profile/edit_profile.html', {'user_profile': user_profile, 'user_form': user_form})

