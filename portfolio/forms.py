from django import forms
from. import models

class StockActions(forms.ModelForm):
    class Meta:
        model = models.BuyingSellingStocks
        fields = ['stock_name','amount','stock_action']

        labels = {
            'stock_name': 'Stock Ticker',
            'amount': 'Number of Stocks',
            'stock_action': 'Stock Action',
        }

class PortfolioAmount(forms.ModelForm):
    class Meta:
        model = models.AddCash
        fields = ['new_cash']

        labels = {
            'new_cash':'Deposit Amount'
        }
