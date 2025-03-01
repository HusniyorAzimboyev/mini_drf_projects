import requests

def get_weather(city):
	url = f"https://open-weather13.p.rapidapi.com/city/{city}/EN"
	headers = {
		"x-rapidapi-key": "54048b746fmshda22903440ad421p1034c5jsn64cb525b2b1b",
		"x-rapidapi-host": "open-weather13.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers).json()
	fahrenheit = response["main"]["temp"]
	celsius = (fahrenheit - 32) * 5/9
	return f'{round(celsius, 2)}°C'
print(get_weather("tashkent"))