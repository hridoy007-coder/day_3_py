import datetime
from playsound import playsound
import time

alarm_hour = int(input("Enter the hour:"))
alarm_minute = int(input("Enter the minute:"))
alarm_second = int(input("Enter the second:"))
alarm_period = input("Enter AM/PM:")

if alarm_period == "pm":
    alarm_hour += 12

while True:
    if alarm_hour == datetime.datetime.now().hour and \
         alarm_minute == datetime.datetime.now().minute and \
         alarm_second == datetime.datetime.now().second:
          print("Alarm is ringing...")
          playsound('alarm.mp3')
          break
    
    time.sleep(3)