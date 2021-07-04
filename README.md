# A Lambda API function to get the top 5 stocks of the day.

A simple backend (read/write to DynamoDB) with a RESTful API endpoint using Amazon API Gateway.

This Lambda uses RapidAPI interface to get the top 5 stocks of the day (updated to current time).

The Lambda function gets NIFTY50 stocks data from the free API : https://rapidapi.com/suneetk92/api/latest-stock-price/ .

By Analyzing the json file it returns the top 5 stocks ordered, with their precentage change of today.

#### The Lambda API is live on AWS here: https://5hpqt52l40.execute-api.us-east-1.amazonaws.com/default/dataLambda
