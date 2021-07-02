import requests


def getStockData():
    url = "https://latest-stock-price.p.rapidapi.com/price"

    querystring = {"Indices": "NIFTY 50"}

    headers = {
        'x-rapidapi-key': "d135343a79msh10005ed1d7011d4p13d3f4jsn116c7b03a7b3",
        'x-rapidapi-host': "latest-stock-price.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text


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
