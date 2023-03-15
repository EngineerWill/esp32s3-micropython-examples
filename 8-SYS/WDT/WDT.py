#---------------------------------------------------------------
# | File        :   WDT.py                               
# | Author      :   Waveshare team                              
# | Function    :   Set WDT 10s and Feed at varying intervals
# | Info        :   WDT test code                          
#---------------------------------------------------------------
# | This version:   V1.0                                        
# | Date        :   2022-03-15                                  
# | Info        :   Basic version                               
#---------------------------------------------------------------
from machine import WDT
import time

# Set the timeout for the watchdog timer
feed_timeout = 3000
wdt = WDT(timeout=feed_timeout)

# Feed the watchdog timer at varying intervals
for i in range(1000, 5000, 250):
    time.sleep_ms(i)
    print("feed_timeout={}, delay {}ms feed success".format(feed_timeout, i))
    wdt.feed()