#---------------------------------------------------------------
# | File        :   key.py                                      
# | Author      :   Waveshare team                              
# | Function    :   When the key is pressed, toggle LED state    
# | Info        :   key test code                               
#---------------------------------------------------------------
# | This version:   V1.0                                        
# | Date        :   2022-03-15                                  
# | Info        :   Basic version                               
#---------------------------------------------------------------
from machine import Pin
import pico_gpio
import time

# Create LED object and turn it off
LED=Pin(pico_gpio.D10,Pin.OUT) 
# Create KEY object
KEY=Pin(pico_gpio.D3,Pin.IN,Pin.PULL_UP) 
# LED state
state=0 

while True:
    # If button is pressed
    if KEY.value()==0: 
        # Debounce
        time.sleep_ms(10) 
        # Confirm button is pressed
        if KEY.value()==0: 
            # Use not statement instead of ~ statement
            state=not state  
            # Toggle LED state
            LED.value(state) 
            # Check if button is released
            while not KEY.value(): 
                time.sleep_ms(50) 