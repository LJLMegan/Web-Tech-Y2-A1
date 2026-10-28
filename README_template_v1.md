# 🚀 Space Bot API Investigation Sheet

**Total Marks: 40**  
**TASK 1: Collect Required API Documentation**

This investigation sheet helps you gather key technical information from the three APIs required for the Space Bot project: **Webex Messaging API**, **ISS Current Location API**, **Weather API** and a **Geocoding API** , plus the Python time module. Also furhter investigate the application of Web Architecture and MVC design pattern in development of the Bot

---

##  Webex Messaging API (4 marks)

| Criteria | Details |
|---------|---------|
| API Base URL | https://webexapis.com/v1 |
| Authentication Method | Bearer Token |
| Endpoint to list rooms | /rooms |
| Endpoint to get messages | /messages/{messageId} |
| Endpoint to send message | /messages/{messageId}|
| Required headers | Authorization: Bearer <TOKEN> and Content-Type: application/json. |
| Sample full GET or POST request | `_______________________________` |

---

##  ISS Current Location API (2 marks)

| Criteria | Details |
|---------|---------|
| API Base URL | http://api.open-notify.org/iss-now.json |
| Endpoint for current ISS location | iss-now.json |
| Sample response format (example JSON) |  

{
  "message": "success",
  "iss_position": {
    "latitude": "-45.3588",
    "longitude": "132.6963"
  },
  "timestamp": 1791971100}
  
---

##  Geocoding API (4 marks)

| Criteria | Details |
|---------|---------|
| Provider used (Choose one) | OpenWeatherMap |
| API Base URL | http://api.openweathermap.org/geo/1.0/zip?zip=E14,GB&appid={API key} |
| Endpoint for geocoding | /geo/1.0/zip |
| Endpoint for reverse geocoding | /geo/1.0/reverse |
| Authentication method | API key |
| Required query parameters | lat=51.5098&lon=-0.1180&limit=5&appid={appId} |
| Sample request with latitude/longitude | lat=51.5098&lon=-0.1180 |
| Sample JSON response (formatted example) |  

[
    {
        "name": "London",
        "local_names": {
            "li": "Londe",
            "hi": "लंदन",
            "lb": "London",
            "la": "Londinium",
            "sd": "لنڊن",
            "hy": "Լոնդոն",
            "sq": "Londra",
            "ky": "Лондон",
            "ln": "Londoni",
            "kk": "Лондон",
            "os": "Лондон",
            "si": "ලන්ඩන්",
            "af": "Londen",
            "rm": "Londra",
            "no": "London",
            "na": "London",
            "hu": "London",
            "bn": "লন্ডন",
            "st": "London",
            "gu": "લંડન",
            "sm": "Lonetona",
            "pl": "Londyn",
            "bs": "London",
            "my": "လန်ဒန်မြို့",
            "tk": "London",
            "id": "London",
            "ascii": "London",
            "bi": "London",
            "az": "London",
            "ee": "London",
            "fj": "Lodoni",
            "br": "Londrez",
            "feature_name": "London",
            "mg": "Lôndôna",
            "sk": "Londýn",
            "to": "Lonitoni",
            "lt": "Londonas",
            "gn": "Londye",
            "lo": "ລອນດອນ",
            "ca": "Londres",
            "am": "ለንደን",
            "ms": "London",
            "en": "London",
            "ar": "لندن",
            "ka": "ლონდონი",
            "gl": "Londres",
            "sl": "London",
            "eu": "Londres",
            "vi": "Luân Đôn",
            "sn": "London",
            "ml": "ലണ്ടൻ",
            "de": "London",
            "qu": "London",
            "io": "London",
            "te": "లండన్",
            "bg": "Лондон",
            "hr": "London",
            "oc": "Londres",
            "co": "Londra",
            "tl": "Londres",
            "sh": "London",
            "is": "Lundúnir",
            "ga": "Londain",
            "av": "Лондон",
            "el": "Λονδίνο",
            "nn": "London",
            "ha": "Landan",
            "om": "Landan",
            "ug": "لوندۇن",
            "tr": "Londra",
            "an": "Londres",
            "ce": "Лондон",
            "ay": "London",
            "yi": "לאנדאן",
            "se": "London",
            "kn": "ಲಂಡನ್",
            "bm": "London",
            "ta": "இலண்டன்",
            "jv": "London",
            "da": "London",
            "tw": "London",
            "wa": "Londe",
            "ht": "Lonn",
            "kv": "Лондон",
            "su": "London",
            "sc": "Londra",
            "uz": "London",
            "tg": "Лондон",
            "ko": "런던",
            "fr": "Londres",
            "or": "ଲଣ୍ଡନ",
            "ig": "London",
            "es": "Londres",
            "bh": "लंदन",
            "ru": "Лондон",
            "lv": "Londona",
            "pa": "ਲੰਡਨ",
            "fa": "لندن",
            "sw": "London",
            "mk": "Лондон",
            "tt": "Лондон",
            "mt": "Londra",
            "mr": "लंडन",
            "yo": "Lọndọnu",
            "mn": "Лондон",
            "et": "London",
            "gv": "Lunnin",
            "th": "ลอนดอน",
            "mi": "Rānana",
            "kl": "London",
            "bo": "ལོན་ཊོན།",
            "so": "London",
            "gd": "Lunnainn",
            "fo": "London",
            "it": "Londra",
            "cy": "Llundain",
            "ur": "لندن",
            "uk": "Лондон",
            "eo": "Londono",
            "ro": "Londra",
            "cu": "Лондонъ",
            "ny": "London",
            "ps": "لندن",
            "ab": "Лондан",
            "wo": "Londar",
            "cv": "Лондон",
            "kw": "Loundres",
            "fi": "Lontoo",
            "pt": "Londres",
            "nl": "Londen",
            "ba": "Лондон",
            "be": "Лондан",
            "zh": "倫敦",
            "fy": "Londen",
            "cs": "Londýn",
            "ku": "London",
            "sv": "London",
            "zu": "ILondon",
            "he": "לונדון",
            "ne": "लन्डन",
            "ff": "London",
            "km": "ឡុងដ៍",
            "ja": "ロンドン",
            "sa": "लन्डन्",
            "sr": "Лондон"
        },
        "lat": 51.5074456,
        "lon": -0.1277653,
        "country": "GB",
        "state": "England"
    }
]

---


##  Weather API (3 marks)

| Criteria | Details |
|---------|---------|
| API Provider (Choose one) | **OpenWeather, OpenWeatherMap (or other – provide details)** |
| API Base URL | `https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}` |
| Endpoint for current weather | `weather` |
| Authentication method | `API key` |
| Required query parameters | `lat, lon, appid` |
| Sample JSON response (formatted example) |  
```json
| {
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
}
```

---

##  Epoch to Human Time Conversion (Python time module) (2 marks)

| Criteria | Details |
|---------|---------|
| Library used | time|
| Function used to convert epoch | strptime() |
| Sample code to convert timestamp |  
``` 
datetime.fromtimestamp(timestamp, tz=timezone.utc) 
```
|
| Output (human-readable time) | import time
from datetime import datetime,timezone

# Get current Unix timestamp
timestamp = int(time.time())
print(timestamp)  # e.g., 1706745600



# Using datetime
timestamp = int(datetime.now().timestamp()) |

---

##  Extended Feature API ( 3 marks)

| Criteria | Details |
|---------|---------|
| API Provider |open-notify.org |
| API Base URL | http://api.open-notify.org/astros.json |
| Endpoint | astros.json |
| Authentication method | No Input |
| Required query parameters | None |
| Sample JSON response (formatted example) |  

{"people": [{"craft": "ISS", "name": "Oleg Kononenko"}, {"craft": "ISS", "name": "Nikolai Chub"}, {"craft": "ISS", "name": "Tracy Caldwell Dyson"}, {"craft": "ISS", "name": "Matthew Dominick"}, {"craft": "ISS", "name": "Michael Barratt"}, {"craft": "ISS", "name": "Jeanette Epps"}, {"craft": "ISS", "name": "Alexander Grebenkin"}, {"craft": "ISS", "name": "Butch Wilmore"}, {"craft": "ISS", "name": "Sunita Williams"}, {"craft": "Tiangong", "name": "Li Guangsu"}, {"craft": "Tiangong", "name": "Li Cong"}, {"craft": "Tiangong", "name": "Ye Guangfu"}], "number": 12, "message": "success"}
```
|

--- 

##  Evaluation – Web Architecture, MVC Design & Security 

In this section, evaluate how web technologies, architecture, and design patterns have been applied in your **AstroBot**. Your responses must relate directly to your implementation and include reflection on your design decisions.

---

###  Web Architecture – Client–Server Model (3 marks)

Explain how the client–server model applies to your AstroBot:

- Identify the **client** 
- Identify the **server(s)** 
- Describe how data flows between:
  - User, AstroBot and APIs

Client: Your Python code running locally on your laptop (your local machine).

Testing Tool: Postman (which you used as a client to inspect the raw HTTP responses).

The Servers: The remote API endpoints like Webex and OpenWeather that wait for those requests and send back data.
Include a **simple block diagram** to illustrate this interaction.



<img width="731" height="523" alt="image" src="https://github.com/user-attachments/assets/dbfc33ae-aa65-4683-98ef-6e1ff40a8051" />

Data Flow : 

User to AstroBot: The user types a command into the Webex group chat. My example, the group chat is called Megan.

AstroBot to Webex API: AstroBot sends a GET request to Webex to read the user's message.

AstroBot to External APIs: AstroBot checks the command (like /weather <city>) and sends a GET request to OpenWeatherMap for data.

APIs back to AstroBot: The APIs send back  JSON data with the results.

AstroBot back to User: AstroBot takes the values, formats them into a clean message, and uses a POST request to send the reply back to the Webex chat.

####  Security Considerations: (3 marks )
- Consider but not limiting to secure handling of API keys and tokens, API rate limiting, and Input validation (e.g., handling user commands safely), include examples from code where necessary to illustrate.

Handling API Keys and Tokens:

Security is managed dynamically at runtime using get_webex_token() and get_api_key(). Rather than storing credentials in plain text, these functions prompt the user via input("Enter your Webex Access Token: ").strip().   
API Rate Limiting:

To protect external servers from excessive requests, the main loop in main() incorporates a polling delay using time.sleep(5). This controls request frequency, avoiding hitting API rate limits or triggering HTTP 429 errors.

Input Validation:

Incoming command strings are sanitized using .strip().lower(). For example, parts[1].strip() cleans up city inputs in the /weather command to remove leading and trailing spaces before building parameters.

###  RESTful API Usage in Your Application (3 marks )

Explain how REST APIs are used in your AstroBot: 

- Describe how HTTP methods (GET, POST) are used

   HTTP method GET is used to read the file, an instance of this could include fetching user messages with Webex API.

   HTTP method POST is used to send data to the server to create new information in the file or web link, an instance of this could be filling in a form.

- Explain how your bot interacts with APIs (Webex, Weather, ISS, Geocoding)  

Webex API: Retrieves active rooms via get_rooms() ([https://webexapis.com/v1/rooms](https://webexapis.com/v1/rooms)), checks for messages using get_latest_message(), and posts replies using send_message().   

OpenWeatherMap API: Converts city names to geographical coordinates via get_city_coordinates() (/geo/1.0/direct) and fetches weather metrics in get_weather() (/data/2.5/weather).   

Open-Notify (ISS) & Reverse Geocoding API: get_iss_location() fetches real-time coordinates from [http://api.open-notify.org/iss-now.json](http://api.open-notify.org/iss-now.json) and passes the coordinates to reverse_geocode() (/geo/1.0/reverse).

- Describe how JSON responses are received and processed  

Responses are put  into standard Python dictionaries using .json(). The bot extracts values using safe lookup methods like .get("items", []) and dictionary keys such as weather.get("main", {}).get("temp", "N/A") to construct formatted output strings.  

Note: Relate your explanation directly to your code for higher grade. 

#### Security Considerations: (2 marks)
- Check response status codes, Handling invalid or unexpected API responses, Avoiding excessive API calls

Before reading data from an API, my code checks if response.status_code != 200:. This ensures the bot only tries to process information if the server request was successful.

###  MVC Design Pattern in AstroBot (3 Marks)

Explain how the **Model–View–Controller (MVC)** pattern applies to your solution:
Provide a short example based on your implementation

| Component   | Description and Example (Relate to your Bot) |
|------------|----------------------------------|
| **Model**  |  The Model handles all the data, such as functions like get_weather() and get_iss_location() fetching data from APIs.
| **View**   |  The View controls what users see by formatting data into readable text messages and sending them to the Webex chat via send_message()
| **Controller** |  The Controller is the main logic in main() that responds to user commands (like /weather or /iss) and decides which function to run.

### 📝 Reflection and Evaluation ( 8 marks )

Reflect on your AstroBot (400 words):

My AstroBot is effective in meeting the Astronomy Club's needs; for example, I used .strip() to remove spaces and tabs at the beginning and end of the string. This makes it more readable for the users of the club. I also used .lower() to make uppercase letters automatically change to lowercase letters. Having this AstroBot automated in a chat room can save time compared to looking it up manually on a browser because, with the commands I made—for example, with /weather <city>—it gets weather information for a city. I have completed a test in the Webex chatroom with this command; although it is effective with cities, it doesn't work well with towns or smaller areas.

I ran into issues with HTTP status codes within the 400 range. I solved them by going on the OpenWeather API. I looked through the documentation and it shows you how to make an API call and the parameters it requires for Postman to complete a GET request. After I understood this, I made the changes to Postman and it came back with an HTTP status code of 200 for OK.

The other API I believe that the Astronomy Club would find useful is "How Many People Are In Space Right Now", and the link for that is [http://api.open-notify.org/astros.json](http://api.open-notify.org/astros.json). I thought that the Astronomy Club would find this useful because not only does this API return the current number of people in space, but additionally, it is also known to return the names and spacecraft those people are on.

Breaking up my code into separate functions (like get_webex_token(), get_rooms(), get_api_key()) helped me keep the code organized compared to putting everything in one massive block, because not only can I work on the separate functions one block at a time, but it also makes it easier to read with comments separating each block of code and explaining the usage and the reason behind specific functions.

Additionally, a future improvement to the effectiveness of the AstroBot is to input more areas, such as rural areas or towns, rather than being limited to just cities. This is in terms of /weather <city>.

I also added comments above my functions or blocks of code not only because if the bot broke then the club would understand the reasoning behind the logic of the code and how to fix it but also to help clarify some functions.



- What challenges did you face when integrating APIs?  
- What security risks did you identify and how were they handled?  
- How could your solution be improved in the future?  

---

 **Tip:** Link your answers directly to your code and examples for higher marks.
### Notes

- Use official documentation for accuracy (e.g. developer.webex.com, locationiq.com or Mapbox, open-notify.org or other ISS API).
- Be prepared to explain your findings to your instructor or demo how you retrieved them using tools like Postman, Curl, or Python scripts.

---

###  Total: /40
