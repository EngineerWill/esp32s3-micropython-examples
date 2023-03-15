#---------------------------------------------------------------
# | File        :   fade.py                                      
# | Author      :   Waveshare team                              
# | Function    :   led fade   
# | Info        :   led test code                               
#---------------------------------------------------------------
# | This version:   V1.0                                        
# | Date        :   2022-03-15                                  
# | Info        :   Basic version                               
#---------------------------------------------------------------

from machine import Pin, PWM
import pico_gpio
import time

# Set the GPIO pin number for the LED
led_fade_num = pico_gpio.D12

# Set the starting and ending duty cycle for the PWM signal
led_fade_start_duty = 0
led_fade_end_duty   = 100

# Create a PWM object for the LED
led_fade = PWM(Pin(led_fade_num))

# Set the frequency of the PWM signal to 1000 Hz
led_fade.freq(1000)

# Set the initial duty cycle of the PWM signal to 0%
led_fade.duty_u16(0)

# Print a message to indicate that the LED fade demo has started
print("led_fade demo")

# Loop forever
while True:
    # Increase the duty cycle of the PWM signal from the starting duty cycle to the ending duty cycle
    for cnt in range(led_fade_start_duty,led_fade_end_duty,1):
        led_fade.duty_u16(int(cnt * 655.36))
        time.sleep_ms(10)
    # Decrease the duty cycle of the PWM signal from the ending duty cycle to the starting duty cycle
    for cnt in range(led_fade_end_duty,led_fade_start_duty,-1):
        led_fade.duty_u16(int(cnt * 655.36))
        time.sleep_ms(10)
