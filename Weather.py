# We are making a weather app that tells you how the weather is in any city you want.
# We will make a window to show the weather using a library called tkinter.


import tkinter as tk  # This is a toolbox that helps us make a window on the screen.
import requests  # This helps us talk to the internet to get weather information.
import time  # This helps us handle time and format it properly.



# This is a function that gets the weather for the city you type.
def getWeather(canvas):
  city = textField.get()  # Get the name of the city from the text box.


  # This is a magic link (API) that gives us the weather when we ask it nicely.
  #You can get API from opeanweathermap as well.
  api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=0f01b24e8096cc9e4674e2e03ad189e4"


  json_data = requests.get(api).json()  # Go to the internet and get the weather in computer language (JSON).


  # json_data: This is the entire JSON response received from the OpenWeather API.
  # It contains all the weather information for the requested city.
  # json_data['weather']: In the API response, "weather" is a list (array) that holds weather condition details.
  # It contains several items and we want the first items from it and for that we use   json_data['weather'][0] .
  # Since "weather" is a list, we access the first element using [0]. This retrieves the first (and usually primary) weather condition.
  # json_data['weather'][0]['main']: "main" is a key inside the first element of "weather" list.
  # It contains the main weather description (e.g., "Clear", "Rain", "Clouds", "Snow").


  # 'weather' contains general weather conditions (like 'Rainy', 'Clear', etc.). The These are keys in the JSON response from the OpenWeather API.
  condition = json_data['weather'][0]['description']  # Find out if it’s sunny, rainy, or cloudy.


  # ---------------------- TEMPERATURE CONVERSION ---------------------- #
  # The OpenWeather API provides temperature in Kelvin.
  # We need to convert it to Fahrenheit using this formula:
  # Fahrenheit = (Kelvin - 273.15) * 1.8 + 32


  temp = int(((json_data['main']['temp'] - 273.15) * 1.8 + 32))  # Convert Kelvin to Fahrenheit



  # Explanation of Conversion:
  # - Kelvin is the default temperature unit from the API.
  # - 273.15 is subtracted to convert Kelvin to Celsius.
  # - The result is multiplied by 1.8 and then added 32 to convert Celsius to Fahrenheit.
  # - 'int()' is used to round the final result to a whole number.


  # ---------------------- OTHER WEATHER DETAILS ---------------------- #
  pressure = json_data['main']['pressure']  # Air pressure in hPa (hectopascal)
  humidity = json_data['main']['humidity']  # Humidity percentage in the air
  wind = json_data['wind']['speed']  # Wind speed in meters per second

#sea level and ground level data
  sea_level = json_data['main'].get('sea_level', 'N/A')  # Sea level pressure
  grnd_level = json_data['main'].get('grnd_level', 'N/A')  # Ground level pressure
  # ---------------------- SUNRISE & SUNSET TIME CONVERSION ---------------------- #
  # The 'sys' section in the JSON response contains system-related information,
  # including sunrise and sunset times in UTC (Universal Coordinated Time).
  # The API provides sunrise & sunset times in seconds since January 1, 1970 (Unix time format).
  # We subtract 21600 seconds (6 hours) to adjust from UTC to a different time zone (likely Central Time, USA).
  # If you're in a different time zone, change this value to match your UTC offset.
  sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
  sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
  # Explanation of time conversion:
  # - 'json_data['sys']['sunrise']' gives the sunrise time in UTC seconds.
  # - 'json_data['sys']['sunset']' gives the sunset time in UTC seconds.
  # - 'time.gmtime()' converts these seconds into a readable time format.
  # - 'time.strftime('%I:%M:%S', ...)' formats the time as HH:MM:SS (12-hour format with AM/PM).
  # ---------------------- FINAL WEATHER DATA DISPLAY ---------------------- #
  # Create a message showing the main weather condition and temperature.
  final_info = condition + "\n" + str(temp) + "°F"
  # Create a message showing extra weather details.
  final_data = "\n" + "Pressure: " + str(pressure)  + "\n" + "Humidity: " + str(
    humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sea Level: " + str(
    sea_level) + "\n" + "Ground level: " + str(
    grnd_level) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset



  # Show the main weather (like "Sunny" and the temperature) on the screen.
  label1.config(text=final_info)


  # Show the extra weather details on the screen.
  label2.config(text=final_data)




# ---------------------- GUI SETUP ---------------------- #
# Now we make a window where everything will appear.
canvas = tk.Tk()


# Make the window 600 pixels wide and 500 pixels tall.
canvas.geometry("600x500")


# Give the window a name at the top.
canvas.title("Weather App")


# Pick a cool font for the details text.
f = ("poppins", 15, "bold")


# Pick a bigger font for the main weather display.
t = ("poppins", 35, "bold")

#label above search box
instruction_label = tk.Label(canvas, text="Put the City Name Below", font=("poppins",12))
instruction_label.pack(pady=10)

# Make a box where you can type a city name.
textField = tk.Entry(canvas, justify='center', width=20, font=t)


# Put the text box in the window and give it space at the top.
textField.pack(pady=20)


# When you open the app, the text box is ready to type in.
textField.focus()


# When you press "Enter," call the getWeather function to show the weather.
textField.bind('<Return>', getWeather)


# Make a label to show the main weather (big text).
label1 = tk.Label(canvas, font=t)
label1.pack()


# Make another label to show extra weather details (smaller text).
label2 = tk.Label(canvas, font=f)
label2.pack()


# Start the app and keep it running.
canvas.mainloop()

