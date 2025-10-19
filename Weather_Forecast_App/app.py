import requests
import tkinter as tk
from tkinter import messagebox

# --- Function to get weather data ---
def get_weather():
    city = city_entry.get()
    api_key = "d0612a433b1924843ecaddab0436db08"  
    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    if not city or city.lower() == "enter city name":
        messagebox.showwarning("Input Error", "Please enter a valid city name!")
        return

    complete_url = f"{base_url}appid={api_key}&q={city}&units=metric"

    try:
        response = requests.get(complete_url)
        data = response.json()
        print(data)  # debug line

        if data.get("cod") != "404":
            city_name = data["name"] 
            country = data["sys"]["country"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"].capitalize()
            wind_speed = data["wind"]["speed"]

            result_label.config(
                text=f"📍 {city_name}, {country}\n"
                     f"🌡️ Temperature: {temperature}°C\n"
                     f"💧 Humidity: {humidity}%\n"
                     f"🌬️ Wind Speed: {wind_speed} m/s\n"
                     f"☁️ Description: {description}"
            )
        else:
            messagebox.showerror("Error", "City not found!")
    except Exception as e:
        messagebox.showerror("Error", f"Unable to fetch data!\n{e}")

# --- GUI setup ---
root = tk.Tk()
root.title("Weather Forecast App")
root.geometry("400x400")
root.config(bg="#d9f0ff")

# Title
title_label = tk.Label(root, text="🌦️ Weather Forecast App", font=("Arial", 16, "bold"), bg="#d9f0ff")
title_label.pack(pady=10)

# City input
city_entry = tk.Entry(root, font=("Arial", 14), width=25, justify="center")
city_entry.pack(pady=10)
city_entry.insert(0, "Enter city name")

# Search button
search_button = tk.Button(root, text="Get Weather", command=get_weather, bg="#4ca3dd", fg="white", font=("Arial", 12, "bold"))
search_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#d9f0ff", justify="left")
result_label.pack(pady=20)

# Footer
footer = tk.Label(root, text="Developed by Mitodru Mridha", font=("Arial", 9, "italic"), bg="#d9f0ff", fg="gray")
footer.pack(side="bottom", pady=10)

root.mainloop()
