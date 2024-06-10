from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . import forms
from django.core.exceptions import ValidationError

# Create your views here.

@login_required(login_url="/accounts/login/")
def portfolio(request):
    if request.method == 'POST':
        form1 = forms.StockActions(request.POST) #post = all the data, files = all the files, they don't come together.
        print(request.POST)
        form2 = forms.PortfolioAmount(request.POST)
        if form1.is_valid():
            #change what is underneath

            vals = form1.save(commit = False)
            print(vals.price)
            if (vals.price is None):
                print("hello")
                form1.add_error('stock_name', 'The stock ticker is incorrect.')


            return redirect('stock_information:stock_info')

        if form2.is_valid():
            return redirect('stock_information:stock_info')

    else:
        form1 = forms.StockActions()
        form2 =forms.PortfolioAmount()

    return render(request, 'portfolio/stock_portfolio.html', {'form1':form1,'form2':form2})



