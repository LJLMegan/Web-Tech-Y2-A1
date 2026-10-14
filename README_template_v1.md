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
| Required headers | `_______________________________` |
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
            "km": "ឡុងដ៍",
            "af": "Londen",
            "kw": "Loundres",
            "ca": "Londres",
            "ko": "런던",
            "tk": "London",
            "mt": "Londra",
            "is": "Lundúnir",
            "am": "ለንደን",
            "la": "Londinium",
            "mk": "Лондон",
            "ay": "London",
            "ee": "London",
            "pa": "ਲੰਡਨ",
            "de": "London",
            "lt": "Londonas",
            "ps": "لندن",
            "gl": "Londres",
            "bn": "লন্ডন",
            "ml": "ലണ്ടൻ",
            "ms": "London",
            "ab": "Лондан",
            "ta": "இலண்டன்",
            "gd": "Lunnainn",
            "wo": "Londar",
            "qu": "London",
            "kn": "ಲಂಡನ್",
            "no": "London",
            "se": "London",
            "he": "לונדון",
            "mg": "Lôndôna",
            "ff": "London",
            "an": "Londres",
            "gn": "Londye",
            "co": "Londra",
            "to": "Lonitoni",
            "io": "London",
            "ny": "London",
            "ln": "Londoni",
            "os": "Лондон",
            "sl": "London",
            "fr": "Londres",
            "hu": "London",
            "uk": "Лондон",
            "be": "Лондан",
            "hr": "London",
            "sw": "London",
            "ja": "ロンドン",
            "fj": "Lodoni",
            "tl": "Londres",
            "pt": "Londres",
            "st": "London",
            "eu": "Londres",
            "vi": "Luân Đôn",
            "feature_name": "London",
            "bo": "ལོན་ཊོན།",
            "wa": "Londe",
            "ce": "Лондон",
            "ur": "لندن",
            "sv": "London",
            "mr": "लंडन",
            "et": "London",
            "jv": "London",
            "gv": "Lunnin",
            "ru": "Лондон",
            "tt": "Лондон",
            "es": "Londres",
            "lb": "London",
            "si": "ලන්ඩන්",
            "lo": "ລອນດອນ",
            "yi": "לאנדאן",
            "ig": "London",
            "uz": "London",
            "ba": "Лондон",
            "mn": "Лондон",
            "th": "ลอนดอน",
            "tw": "London",
            "id": "London",
            "kv": "Лондон",
            "bi": "London",
            "ga": "Londain",
            "br": "Londrez",
            "sn": "London",
            "nn": "London",
            "fo": "London",
            "sh": "London",
            "ky": "Лондон",
            "ku": "London",
            "ka": "ლონდონი",
            "mi": "Rānana",
            "rm": "Londra",
            "zu": "ILondon",
            "az": "London",
            "om": "Landan",
            "ar": "لندن",
            "sa": "लन्डन्",
            "sc": "Londra",
            "el": "Λονδίνο",
            "fi": "Lontoo",
            "te": "లండన్",
            "bs": "London",
            "cu": "Лондонъ",
            "su": "London",
            "zh": "倫敦",
            "cy": "Llundain",
            "bg": "Лондон",
            "sk": "Londýn",
            "nl": "Londen",
            "fa": "لندن",
            "na": "London",
            "tr": "Londra",
            "my": "လန်ဒန်မြို့",
            "fy": "Londen",
            "or": "ଲଣ୍ଡନ",
            "av": "Лондон",
            "eo": "Londono",
            "tg": "Лондон",
            "sd": "لنڊن",
            "en": "London",
            "gu": "લંડન",
            "ascii": "London",
            "it": "Londra",
            "hi": "लंदन",
            "sq": "Londra",
            "bm": "London",
            "hy": "Լոնդոն",
            "cs": "Londýn",
            "oc": "Londres",
            "ht": "Lonn",
            "ug": "لوندۇن",
            "kl": "London",
            "pl": "Londyn",
            "ha": "Landan",
            "sr": "Лондон",
            "yo": "Lọndọnu",
            "ro": "Londra",
            "da": "London",
            "so": "London",
            "li": "Londe",
            "kk": "Лондон",
            "lv": "Londona",
            "cv": "Лондон",
            "sm": "Lonetona",
            "bh": "लंदन",
            "ne": "लन्डन"
        },
        "lat": 51.5074456,
        "lon": -0.1277653,
        "country": "GB",
        "state": "England"
    },
    {
        "name": "City of London",
        "local_names": {
            "es": "City de Londres",
            "pl": "City of London",
            "fr": "Cité de Londres",
            "uk": "Лондонське Сіті",
            "sr": "Сити (Лондон)",
            "zh": "倫敦市",
            "lt": "Londono Sitis",
            "en": "City of London",
            "hi": "सिटी ऑफ लंदन",
            "he": "הסיטי של לונדון",
            "bn": "সিটি অফ লন্ডন",
            "pt": "Cidade de Londres",
            "ko": "시티 오브 런던",
            "ru": "Сити",
            "eo": "Urbo de Londono",
            "ur": "لندن شہر"
        },
        "lat": 51.5156177,
        "lon": -0.0919983,
        "country": "GB",
        "state": "England"
    },
    {
        "name": "London",
        "local_names": {
            "oj": "Baketigweyaang",
            "ka": "ლონდონი",
            "lt": "Londonas",
            "he": "לונדון",
            "iu": "ᓚᓐᑕᓐ",
            "ru": "Лондон",
            "el": "Λόντον",
            "sr": "Лондон",
            "ar": "لندن",
            "ga": "Londain",
            "cr": "ᓬᐊᐣᑕᐣ",
            "th": "ลอนดอน",
            "be": "Лондан",
            "fa": "لندن",
            "lv": "Landona",
            "yi": "לאנדאן",
            "fr": "London",
            "ko": "런던",
            "ug": "لوندۇن",
            "en": "London",
            "bn": "লন্ডন",
            "hy": "Լոնտոն",
            "es": "Londres",
            "ja": "ロンドン"
        },
        "lat": 42.9832406,
        "lon": -81.243372,
        "country": "CA",
        "state": "Ontario"
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
| Library used | `_______________________________` |
| Function used to convert epoch | `_______________________________` |
| Sample code to convert timestamp |  
```  
```
|
| Output (human-readable time) | `_______________________________` |

---

##  Extended Feature API ( 3 marks)

| Criteria | Details |
|---------|---------|
| API Provider |open-notify.org |
| API Base URL | http://api.open-notify.org/astros.json |
| Endpoint | astros.json |
| Authentication method | No Input |
| Required query parameters |  |
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

Include a **simple block diagram** to illustrate this interaction.

####  Security Considerations: (3 marks )
- Consider but not limiting to secure handling of API keys and tokens, API rate limiting, and Input validation (e.g., handling user commands safely), include examples from code where necessary to illustrate.

---

###  RESTful API Usage in Your Application (3 marks )

Explain how REST APIs are used in your AstroBot: 

- Describe how HTTP methods (GET, POST) are used

   HTTP method GET is used to read the file, an instance of this could include fetching user messages with Webex API.

   HTTP method POST is used to send data to the server to create new information in the file or web link, an instance of this could be filling in a form.

- Explain how your bot interacts with APIs (Webex, Weather, ISS, Geocoding)  
- Describe how JSON responses are received and processed  

Note: Relate your explanation directly to your code for higher grade. 

#### Security Considerations: (2 marks)
- Check response status codes, Handling invalid or unexpected API responses, Avoiding excessive API calls

---

###  MVC Design Pattern in AstroBot (3 Marks)

Explain how the **Model–View–Controller (MVC)** pattern applies to your solution:
Provide a short example based on your implementation

| Component   | Description and Example (Relate to your Bot) |
|------------|----------------------------------|
| **Model**  |  |
| **View**   |  |
| **Controller** |  |

---

### 📝 Reflection and Evaluation ( 8 marks )

Reflect on your AstroBot (400 words):

- How effective is your bot in meeting the Astronomy Club’s needs?  
- What design decisions worked well?  
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
