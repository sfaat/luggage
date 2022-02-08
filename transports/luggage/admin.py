from django.contrib import admin
from .models import Price, Customer,Notification

# Register your models here.

admin.site.register(Price)
admin.site.register(Customer)
admin.site.register(Notification)