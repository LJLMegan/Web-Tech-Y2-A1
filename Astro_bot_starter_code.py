#Contains partially completed code with sections for you to complete
#IT IS MANDATORY TO USE THE RESOURCE PROVIDED
#The starter code is structured into functions and modules. You are required to complete the missing sections while maintaining this modular design. Further step by step instructions can be found in the appendix A of this assignment brief.
#For extended features implement it within the existing modular structure. The new feature must be triggered using a new command (e.g., /stars, /moon, /sky) and follow the same approach.
#Use Git for version control. Maintain a repository on GitHub to track your project’s progress and changes. Ensure regular commits for each step with meaningful messages that document your step by step development process.

# =========================
# REQUIRED LIBRARIES
# =========================

import json
import time
from datetime import datetime, timezone

import requests

# =========================
# CONFIGURATION FUNCTIONS
# =========================
DEFAULT_WEBEX_TOKEN = "Enter Webex token here"
DEFAULT_WEATHER_KEY = "Enter API key here"


def get_webex_token():
    choice = input("Use hard-coded Webex token? (y/n): ").strip().lower()
    if choice == "n":
        token = input("Enter your Webex Access Token: ").strip()
        return f"Bearer {token}"
    return f"Bearer {DEFAULT_WEBEX_TOKEN}"


def get_api_key(prompt, hardcoded_key):
    choice = input(f"Use hard-coded {prompt}? (y/n): ").strip().lower()
    if choice == "n":
        token = input(f"Enter your {prompt}: ").strip()
        return token
    return hardcoded_key


# =========================
# WEBEX FUNCTIONS
# =========================
def get_rooms(token):
    url = "https://webexapis.com/v1/rooms"
    headers = {"Authorization": token}
    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code != 200:
        print("Error fetching rooms:", response.status_code)
        return []

    return response.json().get("items", [])


def print_rooms(rooms):
    for room in rooms:
        print(f"Room Title: {room.get('title', 'Unknown')}, Room ID: {room.get('id', 'Unknown')}")


def select_room(rooms):
    while True:
        name = input("What is your room title or ID? ").strip()
        for room in rooms:
            title = str(room.get("title", ""))
            room_id = str(room.get("id", ""))
            if name.lower() in title.lower() or name.lower() == room_id.lower():
                print("Room found:", title)
                return room_id
        print("Room not found.")


def get_latest_message(token, room_id):
    url = "https://webexapis.com/v1/messages"
    params = {"roomId": room_id, "max": 1}
    headers = {"Authorization": token}

    response = requests.get(url, headers=headers, params=params, timeout=10)

    if response.status_code != 200:
        return None, None

    data = response.json().get("items", [])
    if not data:
        return None, None

    latest = data[0]
    return latest.get("id"), latest.get("text", "")


def send_message(token, room_id, message):
    url = "https://webexapis.com/v1/messages"
    headers = {"Authorization": token, "Content-Type": "application/json"}
    data = {"roomId": room_id, "text": message}
    return requests.post(url, headers=headers, data=json.dumps(data), timeout=10)


# =========================
# WEATHER FUNCTIONS
# =========================
def get_city_coordinates(city, api_key):
    url = "https://api.openweathermap.org/geo/1.0/direct"
    params = {"q": city, "limit": 1, "appid": api_key}
    response = requests.get(url, params=params, timeout=10)

    if response.status_code != 200:
        print("Error fetching city coordinates:", response.status_code)
        return None

    data = response.json()
    return data[0] if data else None


def get_weather(city, api_key):
    location = get_city_coordinates(city, api_key)
    if not location:
        return f"Error fetching location for {city}."

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": location["lat"],
        "lon": location["lon"],
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params, timeout=10)
    if response.status_code != 200:
        return "Error fetching weather data."

    weather = response.json()
    city_name = weather.get("name", city)
    country = weather.get("sys", {}).get("country", "Unknown")
    temperature = weather.get("main", {}).get("temp", "N/A")
    description = weather.get("weather", [{}])[0].get("description", "N/A")
    humidity = weather.get("main", {}).get("humidity", "N/A")
    wind_speed = weather.get("wind", {}).get("speed", "N/A")

    return (
        f"Weather for {city_name}, {country}\n"
        f"Temperature: {temperature}°C\n"
        f"Conditions: {description}\n"
        f"Humidity: {humidity}%\n"
        f"Wind speed: {wind_speed} m/s"
    )


# =========================
# ISS FUNCTIONS
# =========================
def reverse_geocode(lat, lon, api_key):
    url = "https://api.openweathermap.org/geo/1.0/reverse"
    params = {"lat": lat, "lon": lon, "limit": 1, "appid": api_key}

    response = requests.get(url, params=params, timeout=10)
    if response.status_code != 200:
        return None

    data = response.json()
    return data[0] if data else None


def get_iss_location(api_key):
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        return "Error fetching ISS location"

    data = response.json()
    position = data.get("iss_position", {})
    timestamp = data.get("timestamp")

    lat = float(position.get("latitude", 0))
    lon = float(position.get("longitude", 0))
    location = reverse_geocode(lat, lon, api_key)

    place = "Over Ocean / No Nearby City"
    if location:
        place = location.get("name") or location.get("state") or location.get("country") or place

    return (
        f"Latitude: {lat}\n"
        f"Longitude: {lon}\n"
        f"Place: {place}\n"
        f"Timestamp: {datetime.fromtimestamp(timestamp, tz=timezone.utc)}"
    )


# =========================
# MAIN BOT LOGIC
# =========================
def main():
    token = get_webex_token()
    weather_key = get_api_key("Weather API key", DEFAULT_WEATHER_KEY)

    rooms = get_rooms(token)
    if not rooms:
        print("This is not a room, please choose another one.")
        return

    print_rooms(rooms)
    room_id = select_room(rooms)

    last_message_id, _ = get_latest_message(token, room_id)

    while True:
        message_id, message_text = get_latest_message(token, room_id)

        if message_id and message_id != last_message_id:
            last_message_id = message_id
            print(f"Message received: {message_id}")

            if not message_text or not message_text.startswith("/"):
                continue

            command = message_text.lower()

            if command == "/help":
                send_message(
                    token,
                    room_id,
                    "Available commands:\n"
                    "/help - Show this help message\n"
                    "/weather <city> - Get weather information for a city\n"
                    "/iss - Get the current location of the ISS\n"
                    "/quit - Shut down the bot\n"
                )

            elif command.startswith("/weather"):
                parts = message_text.split(maxsplit=1)
                if len(parts) < 2:
                    send_message(token, room_id, "Usage: /weather <city>")
                else:
                    city = parts[1].strip()
                    send_message(token, room_id, get_weather(city, weather_key))

            elif command == "/iss":
                send_message(token, room_id, get_iss_location(weather_key))

            elif command == "/quit":
                send_message(token, room_id, "AstroBot shutting down.")
                break

            else:
                send_message(token, room_id, "Unknown command. Use /help")

        time.sleep(5)


if __name__ == '__main__':
    main()
