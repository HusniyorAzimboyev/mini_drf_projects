import requests
from django.conf import settings
import json
def get_weather(city):
	url = f"https://open-weather13.p.rapidapi.com/city/{city}/EN"
	headers = {
		"x-rapidapi-key": settings.RAPIDAPI_KEY,
		"x-rapidapi-host": settings.RAPIDAPI_HOST
	}

	response = requests.get(url, headers=headers).json()
	fahrenheit = response["main"]["temp"]
	celsius = (fahrenheit - 32) * 5/9

	return f'{round(celsius, 2)}°C'
