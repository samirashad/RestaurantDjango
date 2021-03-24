from django.contrib import admin
from .models import Food,FoodCategory

class foodadmin(admin.ModelAdmin):
    list_display=["FoodName","FCategory","Description","Price","ImageFood"]

admin.site.register(FoodCategory)
admin.site.register(Food,foodadmin)

