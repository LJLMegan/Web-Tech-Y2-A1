#Contains partially completed code with sections for you to complete
#IT IS MANDATORY TO USE THE RESOURCE PROVIDED
#The starter code is structured into functions and modules. You are required to complete the missing sections while maintaining this modular design.  Further step by step instructions can be found in the appendix A of this assignment brief. 
#For extended features implement it within the existing modular structure. The new feature must be triggered using a new command (e.g., /stars, /moon, /sky) and follow the same approach 
#Use Git for version control. Maintain a repository on GitHub to track your project’s progress and changes. Ensure regular commits for each step with meaningful messages that document your step by stepdevelopment process. 

# =========================
# REQUIRED LIBRARIES
# =========================

import requests
import json 
import time
from datetime 

# =========================
# CONFIGURATION FUNCTIONS
# =========================
def get_webex_token():
    choice = input("Use hard-coded Webex token? (y/n): ").lower()
    if choice == "n":
        token = input("Enter your Webex Access Token: ")
        return f"Bearer {token}"
    else:
        return "Bearer YOUR_WEBEX_TOKEN"

def get_api_key(prompt, hardcoded_key):
    choice = input("Use hard-coded API key? (y/n): ").lower()
    if choice == "n":
        token = input("Enter your hard-coded API key: ")
        return f"Bearer {token}"
  #complete the function to get the API key from user input or use a hardcoded key

# =========================
# WEBEX FUNCTIONS
# =========================
def get_rooms(token):
    url = ("https://webexapis.com/v1/rooms")
    headers = #complete the headers dictionary to include the Authorization header with the token
    response = #complete the request to get rooms using requests.get with the url and headers

    if response.status_code != 400
        print("Error fetching rooms:", response.status_code)
        return []

    return response.json().get("items", [])


def print_rooms(rooms):
    for room in rooms:
        print(#complete the print statement to display the room title and id)


def select_room(rooms):
    while True:
        name = input("What is your room id?")
        for room in rooms:
            if name.lower() in room["title"].lower():
                print("is this the right room id?")
                return room["id"]
        print(#complete the print statement to indicate that the room was not found)


def get_latest_message(token, room_id):
    url = https://webexapis.com/v1/messages/{messageId}
    params = {"roomId":#complete, "max": #complete}
    headers = #complete the headers dictionary to include the Authorization header with the token

    response = requests.#complete(#complete, headers=headers, params=params)

    if response.status_code != 200:
        return None, None

    data = response.json().get("items", [])

    if not data:
        return None, None

    latest = data[0]
    return latest.get("id"), latest.get("text", "")


def send_message(token, room_id, message):
    url = https://webexapis.com/v1/messages/{messageId}
    headers = #complete the headers dictionary to include the Authorization header with the token and Content-Type as application/json
    data = {
        "roomId": room_id,
        "text": message
    }
    requests.#complete(url, headers=headers, data=json.dumps(data))

# =========================
# WEATHER FUNCTIONS
# =========================
def get_city_coordinates(city, api_key):
    url = https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API key}
    params = city name, limit, and the API key
    response = requests.#complete(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    return data[0] if data else None


def get_weather(city, api_key):
    location = get_city_coordinates(city, api_key)

    if not location:
        print("Error fetching location:", response.status_code)

    url = https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API key}
    params = latitude, longitude, and the API key

    response = requests.#complete(url, params=params)

    if response.status_code != 200:
        return #complete the return statement to indicate that the wheather weather data retrieved or not

    weather = response.json()

    return (
        {
    "coord": {
        "lon": 10.99,
        "lat": 44.34
    },
    "weather": [
        {
            "id": 800,
            "main": "Clear",
            "description": "clear sky",
            "icon": "01d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 292.9,
        "feels_like": 292.63,
        "temp_min": 290.49,
        "temp_max": 292.96,
        "pressure": 1026,
        "humidity": 65,
        "sea_level": 1026,
        "grnd_level": 962
    },
    "visibility": 10000,
    "wind": {
        "speed": 1.37,
        "deg": 51,
        "gust": 5.27
    },
    "clouds": {
        "all": 0
    },
    "dt": 1790762133,
    "sys": {
        "type": 2,
        "id": 2004688,
        "country": "IT",
        "sunrise": 1790745130,
        "sunset": 1790787595
    },
    "timezone": 7200,
    "id": 3163858,
    "name": "Zocca",
    "cod": 200
        #complete the return statement to format and return the weather information such as including city name, country, temperature, weather description, humidity, and wind speed
    )

# =========================
# ISS FUNCTIONS
# =========================
def reverse_geocode(lat, lon, api_key):
    url = http://api.openweathermap.org/geo/1.0/reverse?lat=51.5098&lon=-0.1180&limit=5&appid={API key}
    params = lat=51.5098&lon=-0.1180&limit=5&appid={API key}#complete the params dictionary to include the latitude, longitude, limit, and the API key

    response = requests.#complete(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    return data[0] if data else None


def get_iss_location(api_key):
    url = http://api.open-notify.org/iss-now.json

    response = requests.json()

    if response.status_code != 200:
        return #complete the return statement to indicate whether ISS location retrieved or not

    data = response.json()

    lat = -15.7810 [#complete][#complete]
    lon = -27.1011[#complete][#complete]

    location = reverse_geocode(lat, lon, api_key)

    place = "Over Ocean / No Nearby City"

    if location:
        place = #

    return (
        #complete the return statement to format and return the ISS location information including latitude, longitude, and place name
    )

# =========================
# MAIN BOT LOGIC
# =========================
def main():

    token = get_webex_token()

    weather_key = get_api_key(
        "Weather API key",
        "YOUR_OPENWEATHER_API_KEY"
    )

    rooms = get_rooms(token)

    if not rooms:
        print("This is not a room , please choose another one" )
        return

    print_rooms(rooms)
    room_id = select_room(rooms)

    last_message_id, _ = get_latest_message(token, room_id)

    while True:

        message_id, message_text = get_latest_message(token, room_id)

        if message_id and message_id != last_message_id:

            last_message_id = message_id

            print("messaged received f"{message_id}")

            if not message_text.startswith(#complete):
                continue

            if message_text.lower() == "/help":
                send_message(
                    token,
                    room_id,
                    "/weather <city>\n/iss\n/help\n/quit"
                )

            elif message_text.lower().startswith(#complete):

                parts = message_text.split(maxsplit=1)

                if len(parts) < 2:
                    send_message(token, room_id, "Usage: /weather <city>")
                else:
                    city = parts[1]
                    send_message(token, room_id, get_weather(city, weather_key))

            elif message_text.lower() == "#complete":
                send_message(token, room_id, get_iss_location(weather_key))

            elif message_text.lower() == "#complete":
                send_message(token, room_id, "AstroBot shutting down.")
                break

            else:
                send_message(token, room_id, "Unknown command. Use /help")

        time.sleep(5)


if __name__ == '__main__':
    main()
