from django.shortcuts import render
import requests
import json
import datetime
import pandas as pd
import plotly.express as px

# Create your views here.
with open('config.json') as config_file:
    config = json.load(config_file)
api_key = config["api-key-12"]

def stock_info(request):

    #this section gets the current stock price based on whatever ticker is put into the form.

    if request.method == 'POST':
        ticker = request.POST.get('textbox')
        time = request.POST.get('graph_type')

        api_url_price = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'


        dataprice = requests.get(api_url_price).json()
        if "code" in dataprice:

            dataprice['price'] = "Invalid Stock ticker"
            graph = "<p> Graph not available </p>"
        else:
            dataprice['price'] = round(float(dataprice['price']), 2)


            #this will generate a 1 year price graph of your stock(not ytd).
            t = 0
            title = ''
            if time=='1day':
                start = datetime.date.today()
                interval = "1min"
                title = 'Daily Open Price for Today'
            elif time=='1week':
                start = datetime.date.today() - datetime.timedelta(days=7)
                interval = "1day"
                title = 'Daily Open Price for the week'
            elif time == 'ytd':
                start = datetime.datetime(datetime.date.today().year, month=1, day=1)
                interval = "1day"
                title = 'Daily Open Price, year to date'
            else:
                if time == '1year':
                    t = 1
                    title = 'Daily Open Price for the last year'
                elif time == '5years':
                    t = 5
                    title = 'Daily Open Price for the last 5 years'
                elif time == '10years':
                    t = 10
                    title = 'Daily Open Price for the last 10 years'
                start = datetime.date(datetime.datetime.today().year-t,datetime.datetime.today().month,datetime.datetime.today().day)
                interval = "1day"

            api_url_graph = f'https://api.twelvedata.com/time_series?symbol={ticker}&start_date={start}&interval={interval}&apikey={api_key}'

            data = requests.get(api_url_graph).json()
            data_pd = pd.DataFrame(data['values'])

            data_pd['open'] = data_pd['open'].astype(float)
            data_pd = data_pd.iloc[::-1]

            fig = px.line(data_pd, x='datetime', y='open', title=title)
            graph = fig.to_html(full_html = False)

            #generates ytd graph
            curr_day = datetime.datetime.now()
            first_day_of_year = datetime.datetime(curr_day.year, month=1, day=1)






        return render(request,"stock_information/stock_information.html",{"dataprice":dataprice,"graph":graph})
    else:
        return render(request,"stock_information/stock_information.html")

