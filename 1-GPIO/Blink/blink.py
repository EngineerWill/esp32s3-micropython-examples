#---------------------------------------------------------------
# | File        :   blink.py                                      
# | Author      :   Waveshare team                              
# | Function    :   led blink                       
# | Info        :   led test code                               
#---------------------------------------------------------------
# | This version:   V1.0                                        
# | Date        :   2022-03-15                                  
# | Info        :   Basic version                               
#---------------------------------------------------------------
import machine
import pico_gpio
import time
# pico_gpio.D10 = 35
led_pin = machine.Pin(pico_gpio.D10, machine.Pin.OUT)

while True:
    led_pin.on()
    time.sleep(0.5)
    led_pin.off()
    time.sleep(0.5)