#---------------------------------------------------------------
# | File        :   rgb.py                               
# | Author      :   Waveshare team                              
# | Function    :   rgb fade
# | Info        :   rgb led(ws2812b) test code                          
#---------------------------------------------------------------
# | This version:   V1.0                                        
# | Date        :   2022-03-15                                  
# | Info        :   Basic version                               
#---------------------------------------------------------------
import time
import pico_gpio
from machine import Pin
from neopixel import NeoPixel

max_lum = 100

# Set the pin number for the RGB LED
rgb_led_num = pico_gpio.RGB_PIN

# Create a Pin object for the RGB LED pin
rgb_led_pin = Pin(rgb_led_num, Pin.OUT)

# Create a NeoPixel object for the RGB LED
rgb_led = NeoPixel(rgb_led_pin, 1)

# Set the color order for the NeoPixel object
rgb_led.ORDER = (0, 1, 2, 3)

red = 0
green = 0
blue = 0

print("RGB LED demo")

while True:
    # Fade from black to red
    for i in range(0, max_lum):
        red = i
        blue = max_lum - i
        # Set the color of the NeoPixel
        rgb_led[0] = (red, green, blue)
        rgb_led.write()
        time.sleep_ms(10)

    time.sleep_ms(300)

    # Fade from red to yellow
    for i in range(0, max_lum):
        green = i
        red = max_lum - i
        # Set the color of the NeoPixel
        rgb_led[0] = (red, green, blue)
        rgb_led.write()
        time.sleep_ms(10)

    time.sleep_ms(300)

    # Fade from yellow to green
    for i in range(0, max_lum):
        blue = i
        green = max_lum - i
        # Set the color of the NeoPixel
        rgb_led[0] = (red, green, blue)
        rgb_led.write()
        time.sleep_ms(10)

    time.sleep_ms(300)