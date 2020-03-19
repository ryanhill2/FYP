from django.contrib import admin

# Register your models here.
from .models import Stock, Portfolio
admin.site.register(Stock)
admin.site.register(Portfolio)

