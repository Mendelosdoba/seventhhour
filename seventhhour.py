import tkinter as tk
import tkinter.simpledialog
from tkinter import messagebox
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
  
place = str(input("type location "))
print("Location address:", place) 
location = geolocator.geocode(place)
print((location.latitude, location.longitude)) 
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
date = (datetime(year, month, day))
print(date)
from timezonefinder import TimezoneFinder
obj = TimezoneFinder()
result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
print(result)
geo_location = GeoLocation(place, location.latitude, location.longitude, result)
calendar = ZmanimCalendar(geo_location=geo_location)

chatzos_time: Optional[datetime] = calendar.chatzos()

if chatzos_time is not None:
    print("Chatzos Time:", chatzos_time.strftime("%Y-%m-%d %I:%M:%S %p %Z"))
    
    adjusted_time_6_hours = chatzos_time + timedelta(hours=6)
    adjusted_time_7_hours = chatzos_time + timedelta(hours=7)
    print("Chatzos Time:", chatzos_time.strftime("%I:%M:%S %p"))
    print("We don't make kiddush between", adjusted_time_6_hours.strftime("%I:%M:%S %p"), "&", adjusted_time_7_hours.strftime("%I:%M:%S %p"))
    
else:
    print("Chatzos Time not available for the specified date and time.")



import datetime
delta = datetime.timedelta(days=1)
year = int(input("Enter the year: "))
month = 1
day = 1
date = datetime.date(year, month, day)
end_date = datetime.date(year, 12, 31)
list = []
cha = []
hours = []
mil = 0
num_days = 0
while date <= end_date:
    num_days += 1
    calendar.date = date    # <----  you need to reset the zmanimcalendar date on each iteration
    chatzos_time = calendar.chatzos()
    print(chatzos_time.timestamp())
    milliseconds = int(round(chatzos_time.timestamp()*1000))
    mil += milliseconds
    # print(datetime.datetime.fromtimestamp(milliseconds/1000.0))
    cha.append(chatzos_time)
    list.append(chatzos_time.strftime("%H:%M:%S"))
    hours.append(chatzos_time.strftime("%H"))
    # print(date, chatzos_time.strftime("%H:%M:%S"), end="\n")
    date += delta
total_duration = timedelta()
total_hours = 0
total_minutes = 0
# print(num_days)
print(mil)
# Iterate through chatzos_times
for chatzos_time in cha:
    total_hours += chatzos_time.hour
    total_minutes += chatzos_time.minute
average = mil // num_days
average = datetime.datetime.fromtimestamp(average/1000.0)
formatted_time = average.strftime("%H:%M:%S")
new_time = average + datetime.timedelta(hours=6)
new_time1 = average + datetime.timedelta(hours=7)
new_time = new_time.strftime("%I:%M:%S %p")
new_time1 = new_time1.strftime("%I:%M:%S %p")
print(f"average chatzos don't make kiddush between {new_time} and {new_time1}")

# Calculate the average hour and minute





    





