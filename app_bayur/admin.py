from django.contrib import admin
from app_bayur.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Seller_User)
admin.site.register(Listing_Product)
admin.site.register(Cart)
admin.site.register(CheckoutDetals)