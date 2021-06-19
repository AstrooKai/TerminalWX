import requests
import json

class bcolors:
  BOLD = '\033[1m'
  CYAN = '\033[96m'
  FAIL = '\033[91m'
  END = '\033[0m'  

while True:
  print(f"{bcolors.BOLD}{bcolors.CYAN}TerminalWX v1.0.0{bcolors.END}")
  print("Search Location:")
  weather = requests.get("http://api.weatherapi.com/v1/current.json?key=b55b7411e91d46ae9d855749211806&q=" + input())

  try:
    weather.raise_for_status()
    resp = weather.json()
    info = resp["location"]
    data = resp["current"]
    condition = data["condition"]
    print(f"{bcolors.BOLD}{bcolors.CYAN}Current Weather for {info['name']}, {info['region']} {info['country']}{bcolors.END}")
    print(f"Last Updated: {data['last_updated']}")
    print(" ")
    print(f"Condition: {condition['text']}")
    print(f"Temperature: {data['temp_c']}°C")
    print(f"Heat Index: {data['feelslike_c']}°C")
    print(f"Wind: {data['wind_mph']}mph at {data['wind_degree']}°{data['wind_dir']}")
    print(f"Wind Gust: {data['gust_mph']}mph")
    print(f"Humidity: {data['humidity']}%")
    print(f"Precipitation: {data['precip_mm']}mm")
    print(f"Pressure: {data['pressure_mb']}mb")
    print(f"Cloud Cover: {data['cloud']}%")
    print(f"Visibility: {data['vis_km']}km")
    print(f"UV Index: {data['uv']}")
    print("---------------------------------------")
  
  except requests.exceptions.HTTPError as e:
    print(f"{bcolors.FAIL}{e}{bcolors.END}")
