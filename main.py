from tkinter import *
from config import token
import requests
import time

root = Tk()
root.geometry("600x500")
root.title("Weather App")

def getWeather(city, token=token):
    city = search_city.get()
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric"
    )
    data = response.json()
    
    condition = data["weather"][0]["main"]
    temp = int(data["main"]["temp"])
    min_temp = data["main"]["temp_min"]
    max_temp = data["main"]["temp_max"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    sunrise = time.strftime('%I:%M:%S', time.gmtime(data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(data['sys']['sunset'] - 21600))

    final_temp = condition + "\n" + str(temp) + "°С"
    final_weather = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + str(sunrise) + "\n" + "Sunset: " + str(sunset)

    label1.config(text = final_temp)
    label2.config(text = final_weather)

f1 = ("poppins", 35, "bold")
f2 = ("poppins", 15, "bold")

search_city = Entry(root, font = f1)
search_city.pack(pady = 20)
search_city.focus()
search_city.bind("<Return>", getWeather)

label1 = Label(root, font = f1)
label1.pack()
label2 = Label(root, font = f2)
label2.pack()

mainloop()