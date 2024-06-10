from django.db import models
import json
import requests

class BuyingSellingStocks(models.Model):
    buy = 'buy'
    sell = 'sell'
    actions = [
        (buy,"Buy"),
        (sell,'Sell'),
    ]

    stock_name = models.CharField(max_length=10)
    amount = models.IntegerField()
    #will generate a dropdown field of either buying or selling stock
    stock_action = models.CharField(max_length = 5,choices=actions)
    price = models.FloatField(blank=True, null=True)

    def stock_price(self):
        with open('config.json') as config_file:
            config = json.load(config_file)

        url = f'https://api.twelvedata.com/price?symbol={self.stock_name}&apikey={config["api-key-12"]}'
        data = requests.get(url).json()

        if "code" in data:
            return None

        return round(float(data['price']), 2)

    def save(self,*args,**kwargs):
        self.price = self.stock_price()
        super().save(*args,**kwargs)






    def __str__(self):
        return f'{self.stock_name}({self.amount})@ {self.price}'



class AddCash(models.Model):
    new_cash = models.FloatField()

    def __str__(self):
        return self.new_cash
# Create your models here.
