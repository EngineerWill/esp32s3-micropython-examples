#---------------------------------------------------------------
# | File        :   siren.py                                    
# | Author      :   Waveshare team                              
# | Function    :   buzzer siren                       
# | Info        :   buzzer test code                            
#---------------------------------------------------------------
# | This version:   V1.0                                        
# | Date        :   2022-03-15                                  
# | Info        :   Basic version                               
#---------------------------------------------------------------

from machine import Pin, PWM
import pico_gpio
import time

# Set the GPIO pin number for the buzzer
buzzer_num = pico_gpio.D12

# Set the starting and ending frequency for the buzzer
buzzer_start_freq = 600
buzzer_end_freq   = 1400

# Create a PWM object for the buzzer
buzzer = PWM(Pin(buzzer_num))

# Set the frequency of the PWM signal to 100 Hz
buzzer.freq(100)

# Set the initial duty cycle of the PWM signal to 30%
buzzer_duty = 30
buzzer.duty_u16(int(buzzer_duty * 655.36))

# Print a message to indicate that the buzzer demo has started
print("buzzer demo")

# Loop forever
while True:
    # Increase the frequency of the PWM signal from the starting frequency to the ending frequency
    for cnt in range(buzzer_start_freq,buzzer_end_freq,10):
        buzzer.freq(cnt)
        time.sleep_ms(10)
    # Decrease the frequency of the PWM signal from the ending frequency to the starting frequency
    for cnt in range(buzzer_end_freq,buzzer_start_freq,-10):
        buzzer.freq(cnt)
        time.sleep_ms(10)