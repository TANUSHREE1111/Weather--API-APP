import tkinter as tk
import requests
import time


def getWeather(canvas):
    city= textfield.get()                                  # For Work with input assinging variable
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=926694d65d52c14c5101ab2fcd6f32c4"      # API link from 'WEather Map API'
    
    json_data = requests.get(api).json()                    # For extracting data from Json_data
    condition = json_data['weather'][0]['main']           
   
    temp = int(json_data['main']['temp'] - 273.15)          # In API tem is under "main" ; Substracting of 273.15 is for getting Celcious unite 
    min_temp = int(json_data['main']['temp_min'] - 273.15)  #              "
    max_temp = int(json_data['main']['temp_max'] - 273.15)  #              "
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']

    wind = json_data['wind']['speed']

    sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']-21600))     # (-21600) --->  6 hrs diff from GMtime , ("%I:%M:%S") ---> pattern of Hr,min,sec system
    sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset']-21600))

    final_info = condition + "\n" + str(temp)+ "°C"
    final_data = "\n" + "Max Temp : " + str(max_temp)  + "\n"  + "Min Temp : " + str(min_temp)  + "\n"  + "Pressure : " + str(pressure)  + "\n"  + "Humidity : " + str(humidity) + "\n" +  "Wind Speed : " + str(wind) + "\n" + "Sumrise Time :  " +str(sunrise) + "\n" + "Sunset Time : " + str(sunset)
    
    
    label1.config(text = final_info)          # Assining the Font style of "final_info"
    label2.config(text= final_data)           # Assining the font style of "final_data"





canvas = tk.Tk()                   #Defining UI
canvas.geometry("600x500")           #Geometry of canvas
canvas.title("weather APP")          # Title giving of that API

f= ("poppins",18,"bold")             # Font styling ..Font name,Size,Type
t= ("poppins",40,"bold")

textfield = tk.Entry(canvas,font=t)    # Entry the name of city
textfield.pack(pady=20)                # Pading of the entry
textfield.focus()                      # Entring city name without moving the Cursor
textfield.bind("<Return>", getWeather)

label1 = tk.Label(canvas,font=t)    # Showing of data-1 
label1.pack()                       # Padding the data
label2= tk.Label(canvas,font=f)              #  Showing Data-2
label2.pack()                                # Pading the data


canvas.mainloop()          # defining function