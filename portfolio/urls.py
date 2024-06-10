from django.urls import path,include
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('stock_portfolio/',views.portfolio, name = "stock_portfolio")
]
