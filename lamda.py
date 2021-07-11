import requests
import json
STOCKS_AMOUNT = 5

def getStockData():
    url = "https://latest-stock-price.p.rapidapi.com/price"

    querystring = {"Indices": "NIFTY 50"}

    headers = {
        'x-rapidapi-key': "d135343a79msh10005ed1d7011d4p13d3f4jsn116c7b03a7b3",
        'x-rapidapi-host': "latest-stock-price.p.rapidapi.com"
    }

    all_stocks = json.loads(requests.request("GET", url, headers=headers, params=querystring).text)
    result_top5 = "["
    i = 0
    for stock in all_stocks:
        if i==0:
            i += 1
            continue
        result_top5 += "{\"identifier\": \"" + stock["identifier"] + "\", "
        result_top5 += "\"pChange\": " + str(stock["pChange"]) + "}"
        if(i == STOCKS_AMOUNT):
            break
        result_top5 += " ,"
        i += 1
    result_top5 += "]"
    return result_top5
getStockData()

def lambda_handler(event, context):
    string = getStockData()
    return {
        'statusCode': '200',
        'body': string,
        'headers': {
            'Access-Control-Allow-Origin': 'https://master.d3k6fbvlxi2px3.amplifyapp.com', #used for my Aws Amplify App
            'Content-Type': 'application/json',
        },
    }
