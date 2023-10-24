import tkinter as tk
import tkinter.simpledialog
from datetime import datetime, timedelta
from zmanim.util.geo_location import GeoLocation    
from geopy.geocoders import Nominatim  # You need to install geopy
from geopy.distance import geodesic
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
from timezonefinder import TimezoneFinder 
import pytz
from pytz import timezone 
# Create a geocoder instance (in this case, Nominatim)
from zmanim.zmanim_calendar import ZmanimCalendar
from typing import Optional
calendar = ZmanimCalendar()
def hours_in_week(day_of_week, hour_of_day):
    # Define the number of hours in a day and a week
    hours_per_day = 24
    days_per_week = 7

    # Check if the inputs are within valid ranges
    if 1 <= day_of_week <= days_per_week and 1 <= hour_of_day <= hours_per_day:
        hour_in_week = (day_of_week -1)*hours_per_day + hour_of_day
        return hour_in_week
    else:
        return None  # Return None for invalid inputs

# Example usage

day =  int(input("Please enter day number: ")) # Wednesday (0-based index)
hour = int(input("Please enter hour number: "))  # 2:00 PM
result = hours_in_week(day, hour)

if result is not None:
    print(f"The hour in the week is: {result}")
else:
    print("Invalid input.")
   
#כצנש חלם

if int(result) % 7 == 0:
    print("nogah")
elif int(result) % 7 == 1:
    print("kochav")
elif int(result) % 7 == 2:
    print("levana")
elif int(result) % 7 == 3:
    print("shabsai")
elif int(result) % 7 == 4:
    print("tzedek")
elif int(result) % 7 == 5:
    print("madim")
elif int(result) % 7 == 6:
    print("chama")

def find_madim_occurrences():
    chama_occurrences = []
    
    day = int(input("Enter the day: ")) 
    for hour in range(1, 25):
            result = hours_in_week(day, hour)
            if result is not None and result % 7 == 5:  # Check if it's "chama" time
                chama_occurrences.append((day, hour))

    return chama_occurrences

# Example usage
chama_times = find_madim_occurrences()

if chama_times:
    print("Chama occurrences:")
    for day, hour in chama_times:
        print(f"Day {day}, Hour {hour}")
else:
    print("No chama occurrences found.")


            

# Example usage



#This code defines a function get_madim_hours_for_day(day_of_week) that takes a day of the week (1-7) as input and returns a list of "madim" hours for that day. You can use this function to get the "madim" hours for any day you specify.

#finding longitude, latitude and time zone
# initialize Nominatim API 
geolocator = Nominatim(user_agent="your_unique_user_agent") 
  
# input as a geek 
lad = str(input("type location "))
print("Location address:", lad) 
  
# getting Latitude and Longitude 
location = geolocator.geocode(lad) 
  
print("Latitude and Longitude of the said address:") 
print((location.latitude, location.longitude)) 
latitude = location.latitude
longitude = location.longitude
print(latitude)
print(longitude)
obj = TimezoneFinder() 
  
# returns  
result = obj.timezone_at(lng=location.longitude, lat=location.latitude) 

print("hello")
print(result)
print("Time Zone : ", result) 


year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

yom = datetime(year, month, day)
print(yom)
timezone = pytz.timezone(result)
print(timezone)
# Create a ZmanimCalendar instance
calendar = ZmanimCalendar()

# Get the chatzos time for the specified date and time
chatzos_time: Optional[datetime] = calendar.chatzos()

# Check if chatzos_time is not None (i.e., it was successfully calculated)
if chatzos_time is not None:
    print("Chatzos Time:", chatzos_time)
else:
    print("Chatzos Time not available for the specified date and time.")


netz_time: Optional[datetime] = calendar.hanetz()

if netz_time is not None:
    print("netz Time:", netz_time)
else:
    print("netz Time not available for the specified date and time.")



#=> zmanim.zmanim_calendar.ZmanimCalendar(candle_lighting_offset=18, geo_location=zmanim.util.geo_location.GeoLocation(name='Greenwich, England', latitude=51.4772, longitude=0.0, time_zone=tzfile('/usr/share/zoneinfo/GMT'), elevation=0.0), date=datetime.datetime(2018, 8, 26, 11, 40, 29, 334774), calculator=<zmanim.util.noaa_calculator.NOAACalculator object at 0x10bbf7710>)


# Geocode a location (convert a city name to coordinates)

# Create the tkinter window
root = tk.Tk()
root.geometry("400x400")

def exactly_chatzos():
    city = tk.simpledialog.askstring("Enter City", "Which city are you located in?")
def mean_chatzos():
    city = tk.simpledialog.askstring("Enter City", "Which city are you located in?")

button1 = tk.Button(root, text="exactly chatzos", command=exactly_chatzos)
button1.pack()

# Create the "Chasidim" button
button2 = tk.Button(root, text="mean chatzos", command=mean_chatzos)
button2.pack()

# Start the tkinter main loop
root.mainloop()
