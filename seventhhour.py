import tkinter as tk
import tkinter.simpledialog
from tkinter import messagebox
from datetime import datetime, timedelta
from zmanim.util.geo_location import GeoLocation    
from geopy.geocoders import Nominatim  # You need to install geopy
from geopy.distance import geodesic
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
from timezonefinder import TimezoneFinder
from zmanim.util.math_helper import MathHelper
from dateutil import tz
from itertools import groupby
# from timezonefinder import TimezoneFinder 


# import pytz
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

day =  int(input("Please enter day of week in in 1-7 format: ")) # Wednesday (0-based index)
hour = int(input("Please enter hour number 1-24: "))  # 2:00 PM
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
madim_times = find_madim_occurrences()

if madim_times:
    print("Madim occurrences:")
    for day, hour in madim_times:
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
date = datetime(year, month, day)
print(date)

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
    print("We don't make kiddush between", adjusted_time_6_hours.strftime("%I:%M:%S %p"), "&", adjusted_time_7_hours.strftime("%I:%M:%S %p"), "if we go by exact chatzos")
    
else:
    print("Chatzos Time not available for the specified date and time.")

selected_tz = tz.gettz(result)
start_date = datetime(year, 1, 1)
end_date = datetime(year, 12, 31)
date_list = [start_date + timedelta(days=x) for x in range((end_date-start_date).days+1)]
dst_groups = groupby(date_list, lambda d:selected_tz.dst(datetime(year, d.month, d.day)))
#lambda short way to write function
#how to group datelist by running selected_tz with d parameter which we will give 
#take 2 parameters date_list and how to group list by dst function . the function has d parameter
dst_counts = [list([offset, len(list(g))]) for offset, g in dst_groups]
print("S")
extra_seconds = 0
print(dst_counts)
for i, (offset, count) in enumerate(dst_counts):   
    if i == 1:
        extra_seconds += int(count)

import datetime
delta = datetime.timedelta(days=1)
year = int(input("Enter the year: "))
month = 1
day = 1
date = datetime.date(year, month, day)
end_date = datetime.date(year, 12, 31)

mil = 0
num_days = 0
start_time = "00:00:00"
while date <= end_date:
    num_days += 1
    calendar.date = date 
    chatzos_time = calendar.chatzos()
    chatzos_time_str = chatzos_time.strftime("%H:%M:%S")
    
     #print(chatzos_time.timestamp())
  
    from datetime import datetime
    midnight = datetime.strptime(start_time, "%H:%M:%S")
    # print(midnight)
    t2 = datetime.strptime(chatzos_time_str, "%H:%M:%S")
    # print(t2)
    delta1 = t2 - midnight
    
    milliseconds = delta1.total_seconds()
   
    mil += milliseconds
    date += delta
    # print(date, chatzos_time.strftime("%H:%M:%S"), end="\n")
    
# print(num_days)
print("num_days", num_days)
# Iterate through chatzos_times
print("mil", mil)
mil -= extra_seconds*3600
print("mil", mil)
average =  mil // num_days
print("average", round(average))



# In the timezone 'Europe/Madrid', the days in which the DST change is made in 2021 are 28/03/2021 and 31/10/2021
#is_dst_change(day=datetime.datetime(year=2021, month=3, day=28), timezone = 'Europe/Madrid')  # This should return True





def seconds_to_time(average):
    hours, remainder = divmod(average, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Determine whether it's AM or PM
    period = "am" if hours < 12 else "pm"

    # Convert to 12-hour format
    if hours == 0:
        hours = 12
    elif hours > 12:
        hours -= 12

    
    return f"{int(hours):02d}:{int(minutes):02d} {period}"
time_representation = seconds_to_time(average)
print("time_representation", time_representation)
seconds = average

seconds = seconds % (24 * 3600)
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60


    
       
print("%d:%02d:%02d" % (hour, minutes, seconds))
print("%d:%02d:%02d" % (hour+7, minutes, seconds))

print(f"we don't make kiddush between {int(hour+6):02d}:{int(minutes):02d}:{int(seconds):02d} & {int(hour+7):02d}:{int(minutes):02d}:{int(seconds):02d} for {place}")
#formatted_time = average.strftime("%H:%M:%S")
#new_time = average + datetime.timedelta(hours=6)
#new_time1 = average + datetime.timedelta(hours=7)
#new_time = new_time.strftime("%I:%M:%S %p")
#new_time1 = new_time1.strftime("%I:%M:%S %p")
#print(f"average chatzos don't make kiddush between {new_time} and {new_time1}")

# Calculate the average hour and minute





    