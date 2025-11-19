# Day-11/main.py ← YE NAYA CODE USE KAR (100% chalega)

import requests

def get_weather(city):
    # Ye API key 2025 tak chalegi + free hai
    API_KEY = "b6907d289e10d714a6e88b30761fae22"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        r = requests.get(url)
        data = r.json()
        
        if data.get("cod") == "404":
            print("City nahi mila bhai!")
            return
            
        name = data["name"]
        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        hum = data["main"]["humidity"]
        desc = data["weather"][0]["description"]
        
        print(f"\n{name.upper()} KA MAUSAM")
        print(f"🌡  Temperature  : {temp}°C")
        print(f"🌡  Feel like       : {feels}°C")
        print(f"💧 Humidity       : {hum}%")
        print(f"☁  Mausam        : {desc}")
        
    except:
        print("Internet off hai ya kuch gadbad hai!")

print("LIVE WEATHER APP")
city = input("City ka naam daal (jaise Delhi, Mumbai): ")
get_weather(city)