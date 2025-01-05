import tkinter as tk
from tkinter import messagebox
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_weather():
    """Fetches weather data based on user input and updates the GUI."""
    city = city_entry.get()
    api_key = os.getenv("API_KEY")  # Retrieve the API key from environment variable
    if not api_key:
        messagebox.showerror("Error", "API key not found.")
        return
    
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
        
        # Extract weather details
        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        
        # Update labels with weather information
        result_label.config(
            text=f"Weather in {city_name}, {country}:\n"
                 f"Temperature: {temperature}°C\n"
                 f"Condition: {weather.capitalize()}",
            fg="black"
        )
    except requests.exceptions.HTTPError as http_err:
        messagebox.showerror("HTTP Error", f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        messagebox.showerror("Request Error", f"Request error occurred: {req_err}")
    except KeyError:
        result_label.config(text="City not found. Please check the city name.", fg="red")

# Create the main tkinter window
app = tk.Tk()
app.title("Weather App")
app.geometry("400x300")

# Title label
title_label = tk.Label(app, text="Weather App", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# City entry field
city_label = tk.Label(app, text="Enter City Name:", font=("Arial", 12))
city_label.pack(pady=5)

city_entry = tk.Entry(app, font=("Arial", 12), width=25)
city_entry.pack(pady=5)

# Get Weather button
get_weather_button = tk.Button(app, text="Get Weather", font=("Arial", 12), command=get_weather)
get_weather_button.pack(pady=10)

# Label to display the weather results
result_label = tk.Label(app, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the tkinter main loop
app.mainloop()