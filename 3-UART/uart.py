#---------------------------------------------------------------
# | File        :   uart.py                                    
# | Author      :   Waveshare team                              
# | Function    :   uart send and read                      
# | Info        :   uart test code                            
#---------------------------------------------------------------
# | This version:   V1.0                                        
# | Date        :   2022-03-15                                  
# | Info        :   Basic version                               
#---------------------------------------------------------------
from machine import UART
import pico_gpio
import time

uart1 = UART(1, baudrate=115200, tx=pico_gpio.D0, rx=pico_gpio.D1)
while True:
    uart1.write('Hello World!\r\n')
    while(uart1.any()):
        data = uart1.read()
        print(data)
    time.sleep_ms(1000)
    


