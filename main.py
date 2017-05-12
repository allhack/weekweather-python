import requests
import constants
import datetime

print("This is program which knows the weather around the world!")
print("Enter your city in English: ")
city = input()
print("Enter 'today', 'tomorrow', or 'week'")
days = input()
print()
r = requests.get("""http://api.openweathermap.org/data/2.5/forecast/daily?q=""" +
                 city + """&cnt=""" + str(7) + """&appid=""" + constants.TOKEN)
j = r.json()

# udate = j["list"][0]["dt"]
# date = datetime.datetime.fromtimestamp(int(udate)).strftime('%Y-%m-%d')
# print(date)

n = 0
if days == 'week':
    while n < 7:
        udate = j["list"][n]["dt"]
        date = datetime.datetime.fromtimestamp(int(udate)).strftime('%Y-%m-%d')
        temp_min = j["list"][n]["temp"]["min"]
        temp_max = j["list"][n]["temp"]["max"]
        weather = j["list"][n]["weather"][0]["description"]
        print(date)
        print("Temp min: " + str(temp_min))
        print("Temp max: " + str(temp_max))
        print("Weather: " + weather)
        print()
        n = n + 1
elif days == 'tomorrow':
    udate = j["list"][1]["dt"]
    date = datetime.datetime.fromtimestamp(int(udate)).strftime('%Y-%m-%d')
    temp_min = j["list"][1]["temp"]["min"]
    temp_max = j["list"][1]["temp"]["max"]
    weather = j["list"][1]["weather"][0]["description"]
    print(date)
    print("Temp min: " + str(temp_min))
    print("Temp max: " + str(temp_max))
    print("Weather: " + weather)
    print()
elif days == 'today':
    udate = j["list"][0]["dt"]
    date = datetime.datetime.fromtimestamp(int(udate)).strftime('%Y-%m-%d')
    temp_min = j["list"][0]["temp"]["min"]
    temp_max = j["list"][0]["temp"]["max"]
    weather = j["list"][0]["weather"][0]["description"]
    print(date)
    print("Temp min: " + str(temp_min))
    print("Temp max: " + str(temp_max))
    print("Weather: " + weather)
    print()
