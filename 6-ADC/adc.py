#---------------------------------------------------------------
# | File        :   adc.py                               
# | Author      :   Waveshare team                              
# | Function    :   read usb and A1-3 voltage
# | Info        :   adc test code                          
#---------------------------------------------------------------
# | This version:   V1.0                                        
# | Date        :   2022-03-15                                  
# | Info        :   Basic version                               
#---------------------------------------------------------------
from machine import Pin, ADC
import pico_gpio
import time

# Initialize ADC objects for the USB and three other pins (A1, A2, and A3)
USB_ADC = ADC(Pin(pico_gpio.USB_ADC), atten=ADC.ATTN_11DB)
A1_ADC = ADC(Pin(pico_gpio.A1), atten=ADC.ATTN_11DB)
A2_ADC = ADC(Pin(pico_gpio.A2), atten=ADC.ATTN_11DB)
A3_ADC = ADC(Pin(pico_gpio.A3), atten=ADC.ATTN_11DB)

while True:
    print("/*********** ADC TEST ***********/")

    # Read the voltage from the USB pin and print it to the console
    ADC_VOL = USB_ADC.read_uv() / 1000.0 / 1000.0*2
    print("USB VOL = {:.2F}V".format(ADC_VOL))

    # Read the voltage from the A1 pin and print it to the console
    ADC_VOL = A1_ADC.read_uv() / 1000.0 / 1000.0
    print("A1 VOL  = {:.2F}V".format(ADC_VOL))

    # Read the voltage from the A2 pin and print it to the console
    ADC_VOL = A2_ADC.read_uv() / 1000.0 / 1000.0
    print("A2 VOL  = {:.2F}V".format(ADC_VOL))

    # Read the voltage from the A3 pin and print it to the console
    ADC_VOL = A3_ADC.read_uv() / 1000.0 / 1000.0
    print("A3 VOL  = {:.2F}V".format(ADC_VOL))

    # Wait for 1 second before taking the next reading
    time.sleep_ms(1000)