from django.shortcuts import render

# Create your views here.
def intro(request):
    return render(request, 'main/intro.html')


def home(request):
    return render(request, 'main/home.html')


def login(request):
    return render(request, 'main/login.html')


def register(request):
    return render(request, 'main/register.html')


def profile(request):
    return render(request, 'main/profile.html')


def about_us(request):
    return render(request, 'main/about-us.html')


def blog_details(request):
    return render(request, 'main/blog-details.html')


def blog_grid(request):
    return render(request, 'main/blog-grid.html')

def blog_list(request):
    return render(request, 'main/blog-list.html')


def cart(request):
    return render(request, 'main/cart.html')

def catagory(request):
    return render(request, 'main/catagory.html')

def change_password(request):
    return render(request, 'main/change-password.html')

def checkout_bank(request):
    return render(request, 'main/checkout-bank.html')

def checkout_cash(request):
    return render(request, 'main/checkout-cash.html')

def checkout_payment(request):
    return render(request, 'main/checkout-payment.html')

def checkout(request):
    return render(request, 'main/checkout.html')

def contact(request):
    return render(request, 'main/contact.html')

def edit_profile(request):
    return render(request, 'main/edit-profile.html')

def featured_prodects(request):
    return render(request, 'main/featured-prodects.html')

def flash_sale(request):
    return render(request, 'main/flash-sale.html')

def forget_password_success(request):
    return render(request, 'main/forget-password-success.html')

def forget_password(request):
    return render(request, 'main/forget-password.html')

def message(request):
    return render(request, 'main/message.html')

def my_order(request):
    return render(request, 'main/my-order.html')

def notifications(request):
    return render(request, 'main/notifications.html')


def notifications_details(request):
    return render(request, 'main/notifications-details.html')

def offline(request):
    return render(request, 'main/offline.html')


def otp_confirm(request):
    return render(request, 'main/otp-confirm.html')

def otp(request):
    return render(request, 'main/otp.html')


def pages(request):
    return render(request, 'main/pages.html')

def payment_success(request):
    return render(request, 'main/payment-success.html')


def privacy_policy(request):
    return render(request, 'main/privacy-policy.html')

def settings(request):
    return render(request, 'main/settings.html')

def shop_grid(request):
    return render(request, 'main/shop-grid.html')


def shop_list(request):
    return render(request, 'main/shop-list.html')


def single_product(request):
    return render(request, 'main/single-product.html')


def sub_catagory(request):
    return render(request, 'main/sub-catagory.html')


def support(request):
    return render(request, 'main/support.html')

def wishlist_grid(request):
    return render(request, 'main/wishlist-grid.html')

def wishlist_list(request):
    return render(request, 'main/wishlist-list.html')
