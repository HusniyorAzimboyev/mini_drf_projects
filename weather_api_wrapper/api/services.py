import requests
from django.conf import settings
def get_weather(city):
	url = f"https://open-weather13.p.rapidapi.com/city/{city}/EN"
	headers = {
		"x-rapidapi-key": settings.RAPIDAPI_KEY,
		"x-rapidapi-host": settings.RAPIDAPI_HOST
	}

	response = requests.get(url, headers=headers).json()
	if response["cod"]!=200:
		return response
	print("api status code - ",response["cod"])

	fahrenheit = response["main"]["temp"]
	celsius = (fahrenheit - 32) * 5/9

	return [{"city_name":response["name"],
			"temp":f'{round(celsius, 2)}°C',
			"country":response["sys"]["country"],
			"wind_speed":response["wind"]["speed"]},response]
