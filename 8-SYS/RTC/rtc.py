#---------------------------------------------------------------
# | File        :   rtc.py                               
# | Author      :   Waveshare team                              
# | Function    :   set the RTC time and run                   
# | Info        :   RTC test code                            
#---------------------------------------------------------------
# | This version:   V1.0                                        
# | Date        :   2022-03-15                                  
# | Info        :   Basic version                               
#---------------------------------------------------------------
import machine
import time

# Set up the RTC
rtc = machine.RTC()

# Set the current time
# year, month, day, weekday, hours, minutes, seconds, subseconds
rtc.datetime((2023, 3, 15, 2, 11, 59, 30, 0))
help(rtc.datetime())
# Wait for 5 seconds
time.sleep(1)


while True:
    # Get the current time from the RTC
    current_time = rtc.datetime()
    # Print the current time
    print(current_time)
    time.sleep(1)