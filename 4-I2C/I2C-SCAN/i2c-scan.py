#---------------------------------------------------------------
# | File        :   i2c-scan.py                               
# | Author      :   Waveshare team                              
# | Function    :   i2c scan
# | Info        :   i2c test code                          
#---------------------------------------------------------------
# | This version:   V1.0                                        
# | Date        :   2022-03-15                                  
# | Info        :   Basic version                               
#---------------------------------------------------------------
from machine import Pin, I2C
import pico_gpio

# create an I2C object with SCL on pin D9 and SDA on pin D8
bus = I2C(1, scl=Pin(pico_gpio.D9), sda=Pin(pico_gpio.D8), freq=400_000)

# scan the I2C bus for connected devices and print their addresses
print(bus.scan())



