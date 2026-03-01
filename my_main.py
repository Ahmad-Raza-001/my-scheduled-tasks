import os
import requests
from twilio.rest import Client

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("API_KEY") 
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")


weather_params = {
    "lat": 51.507351,
    "lon":-0.127758,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☔" ,
        from_= '+16617624598',
        to='+923126522154'
    )
    print(message.status)
