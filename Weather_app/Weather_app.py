import requests

print("===== WEATHER APP =====")

api_key = "8ARNMqo7uXgU5NTweEmWn46Hvewjcp1PtqfXTKDZTj29"

city = input("Enter City Name: ")

url = (
    f"https://api.openweathermap.org/data/2.5/weather?"
    f"q={city}&appid={api_key}&units=metric"
)

response = requests.get(url)

data = response.json()

# Debug
print(data)

if response.status_code == 200:

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]

    print("\n===== WEATHER DETAILS =====")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", weather)

else:
    print("\nError:", data["message"])
