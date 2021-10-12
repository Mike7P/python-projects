import datetime
from pytz import timezone
import pytz

def check_no_13(hour, min):
  total = hour + min
  if hour == 13 or min == 13 or total == 13:
    print("Warning! There are numbers in the time that are equal to 13!")

def am_or_pm(hour):
  if hour < 12:
    am_pm = "am"
  else: am_pm = "pm"
  return am_pm

def calculate_sleep_time(wake_time, wakeup_response, hours_to_sleep):
  w2 = (wakeup_time - (hours_to_sleep + wakeup_response)) % 24
  w2h = int(w2//1)
  w2m = int(w2%1*60)
  print('\n'f"You should go to sleep at {w2h}:{w2m}{am_or_pm(w2h)}")
  check_no_13(w2h, w2m)

def calculate_wakeup_time(tz_hour, tz_min, age, wakeup):
      bed_time = (tz_hour) + (tz_min / 60)
      w2 = ((bed_time) + (age + wakeup)) % 24
      w2h = int(w2//1)
      w2m = int(w2%1*60)
      print('\n'f"You should wake up at {w2h}:{w2m}{am_or_pm(w2h)}")
      check_no_13(w2h, w2m)


time_zones = pytz.all_timezones

dt_utcnow = datetime.datetime.now()

buffer = 15
under_18_hours = 9
over_18_hours = 7.5

tz_response = input("Would you like to see a list of timezones to choose? ").lower()

if tz_response == 'yes':
  print(time_zones)

chosen_timezone = input('\n'"Please enter your required timezone, including correct casing: ")

chosen_timezone_time = dt_utcnow.astimezone(pytz.timezone(chosen_timezone))
print('\n'f"This is the current time in your chosen timezone: {chosen_timezone_time.hour}:{chosen_timezone_time.minute}{am_or_pm(chosen_timezone_time.hour)}")

sleep_now_response = input("Would you like to sleep now? Yes or No? ").lower()

wakeup_response = input("How often do you wake up at night?: ")
wakeup_response = int(wakeup_response)
wakeup_response = ((wakeup_response * 15) + buffer) / 60

if sleep_now_response == 'yes':
  age = int(input("How old are you? "))
  if age <= 18:
    calculate_wakeup_time(chosen_timezone_time.hour, chosen_timezone_time.minute, under_18_hours, wakeup_response)
  else:
    calculate_wakeup_time(chosen_timezone_time.hour, chosen_timezone_time.minute, over_18_hours, wakeup_response)
else:
  wakeup_time = int(input("What time would you like to wake up?: "))
  age = int(input("How old are you? "))
  if age <= 18:
    calculate_sleep_time(wakeup_time, wakeup_response, under_18_hours)
  else:
    calculate_sleep_time(wakeup_time, wakeup_response, over_18_hours)


