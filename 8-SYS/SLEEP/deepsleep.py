#---------------------------------------------------------------
# | File        :   deepsleep.py                               
# | Author      :   Waveshare team                              
# | Function    :   deepsleep 10s and reset                 
# | Info        :   deepsleep test code                          
#---------------------------------------------------------------
# | This version:   V1.0                                        
# | Date        :   2022-03-15                                  
# | Info        :   Basic version                               
#---------------------------------------------------------------
import machine
# Set the deep sleep time to 10 seconds
DEEP_SLEEP_TIME = 10000

# Put the ESP32S3 into deep sleep mode
machine.deepsleep(DEEP_SLEEP_TIME)

# The code will not reach this point
print('This will not be printed')