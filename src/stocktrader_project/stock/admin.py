from django.contrib import admin

# Register your models here.
from .models import Stock, Order

admin.site.register(Stock)
admin.site.register(Order)
