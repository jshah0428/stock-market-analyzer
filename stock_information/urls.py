from django.urls import path,include
from . import views

app_name = 'stock_information'
urlpatterns = [
    path('stock_info/',views.stock_info, name = "stock_info")
]
