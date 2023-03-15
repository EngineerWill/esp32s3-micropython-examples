
#---------------------------------------------------------------
# | File        :   pico-lcd-1.3.py                                    
# | Author      :   Waveshare team                              
# | Function    :   Pico-LCD-1.3 test                      
# | Info        :   spi test code                            
#---------------------------------------------------------------
# | This version:   V1.0                                        
# | Date        :   2022-03-15                                  
# | Info        :   Basic version                               
#---------------------------------------------------------------
from machine import Pin,SPI,PWM
import pico_gpio
import framebuf
import time
import os


DC   = pico_gpio.D8
CS   = pico_gpio.D9
SCK  = pico_gpio.D10
MOSI = pico_gpio.D11
RST  = pico_gpio.D12
BL   = pico_gpio.D13

keyA_num = pico_gpio.D15
keyB_num = pico_gpio.D17
keyX_num = pico_gpio.D19
keyY_num = pico_gpio.D21
    
up_num   = pico_gpio.D2
down_num = pico_gpio.D18
left_num = pico_gpio.D16
right_num= pico_gpio.D20
ctrl_num = pico_gpio.D3

class LCD_1inch3(framebuf.FrameBuffer):
    def __init__(self):
        self.width = 240
        self.height = 240
        
        self.cs = Pin(CS,Pin.OUT)
        self.rst = Pin(RST,Pin.OUT)
        
        self.cs(1)
        self.spi = SPI(1)
        self.spi = SPI(1,1000_000)
        self.spi = SPI(1,100000_000,polarity=0, phase=0,sck=Pin(SCK),mosi=Pin(MOSI),miso=None)
        self.dc = Pin(DC,Pin.OUT)
        self.dc(1)
        self.buffer = bytearray(self.height * self.width * 2)
        super().__init__(self.buffer, self.width, self.height, framebuf.RGB565)
        self.init_display()
        
        self.red   =   0x07E0
        self.green =   0x001f
        self.blue  =   0xf800
        self.white =   0xffff
        
    def write_cmd(self, cmd):
        self.cs(1)
        self.dc(0)
        self.cs(0)
        self.spi.write(bytearray([cmd]))
        self.cs(1)

    def write_data(self, buf):
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(bytearray([buf]))
        self.cs(1)

    def init_display(self):
        """Initialize dispaly"""  
        self.rst(1)
        self.rst(0)
        self.rst(1)
        
        self.write_cmd(0x36)
        self.write_data(0x70)

        self.write_cmd(0x3A) 
        self.write_data(0x05)

        self.write_cmd(0xB2)
        self.write_data(0x0C)
        self.write_data(0x0C)
        self.write_data(0x00)
        self.write_data(0x33)
        self.write_data(0x33)

        self.write_cmd(0xB7)
        self.write_data(0x35) 

        self.write_cmd(0xBB)
        self.write_data(0x19)

        self.write_cmd(0xC0)
        self.write_data(0x2C)

        self.write_cmd(0xC2)
        self.write_data(0x01)

        self.write_cmd(0xC3)
        self.write_data(0x12)   

        self.write_cmd(0xC4)
        self.write_data(0x20)

        self.write_cmd(0xC6)
        self.write_data(0x0F) 

        self.write_cmd(0xD0)
        self.write_data(0xA4)
        self.write_data(0xA1)

        self.write_cmd(0xE0)
        self.write_data(0xD0)
        self.write_data(0x04)
        self.write_data(0x0D)
        self.write_data(0x11)
        self.write_data(0x13)
        self.write_data(0x2B)
        self.write_data(0x3F)
        self.write_data(0x54)
        self.write_data(0x4C)
        self.write_data(0x18)
        self.write_data(0x0D)
        self.write_data(0x0B)
        self.write_data(0x1F)
        self.write_data(0x23)

        self.write_cmd(0xE1)
        self.write_data(0xD0)
        self.write_data(0x04)
        self.write_data(0x0C)
        self.write_data(0x11)
        self.write_data(0x13)
        self.write_data(0x2C)
        self.write_data(0x3F)
        self.write_data(0x44)
        self.write_data(0x51)
        self.write_data(0x2F)
        self.write_data(0x1F)
        self.write_data(0x1F)
        self.write_data(0x20)
        self.write_data(0x23)
        
        self.write_cmd(0x21)

        self.write_cmd(0x11)

        self.write_cmd(0x29)

    def show(self):
        self.write_cmd(0x2A)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0xef)
        
        self.write_cmd(0x2B)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0x00)
        self.write_data(0xEF)
        
        self.write_cmd(0x2C)
        
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(self.buffer)
        self.cs(1)
        
  
if __name__=='__main__':
    pwm = PWM(Pin(BL))
    pwm.freq(1000)
    pwm.duty_u16(32768)#max 65535

    LCD = LCD_1inch3()
    #color BRG
    LCD.fill(LCD.white)
    LCD.show()
    LCD.show()
    LCD.text("ESP32-S3-Pico",20,20,LCD.red)
    LCD.text("Pico-LCD-1.3",20,40,LCD.blue)
    LCD.text("Waveshare",20,60,LCD.green)
    
    
    
    LCD.hline(10,10,220,LCD.blue)
    LCD.hline(10,230,220,LCD.blue)
    LCD.vline(10,10,220,LCD.blue)
    LCD.vline(230,10,220,LCD.blue)
    
    
    # LCD.rect(12,12,20,20,LCD.red)
    # LCD.rect(12,103,20,20,LCD.red)
    # LCD.rect(190,12,20,20,LCD.red)
    # LCD.rect(190,103,20,20,LCD.red)
    
    # LCD.show()
    # time.sleep(3)
    # LCD.fill(LCD.white)
    LCD.show()
    keyA    = Pin(keyA_num,Pin.IN,Pin.PULL_UP)
    keyB    = Pin(keyB_num,Pin.IN,Pin.PULL_UP)
    keyX    = Pin(keyX_num ,Pin.IN,Pin.PULL_UP)
    keyY    = Pin(keyY_num ,Pin.IN,Pin.PULL_UP)
    
    up      = Pin(up_num,Pin.IN,Pin.PULL_UP)
    dowm    = Pin(down_num,Pin.IN,Pin.PULL_UP)
    left    = Pin(left_num,Pin.IN,Pin.PULL_UP)
    right   = Pin(right_num,Pin.IN,Pin.PULL_UP)
    ctrl    = Pin(ctrl_num,Pin.IN,Pin.PULL_UP)
    
    while(1):
        if keyA.value() == 0:
            LCD.fill_rect(190,15,30,30,LCD.red)
        else :
            LCD.fill_rect(190,15,30,30,LCD.white)
            LCD.rect(190,15,30,30,LCD.red)
            
            
        if(keyB.value() == 0):
            LCD.fill_rect(190,75,30,30,LCD.red)
        else :
            LCD.fill_rect(190,75,30,30,LCD.white)
            LCD.rect(190,75,30,30,LCD.red)
            
            
        if(keyX.value() == 0):
            LCD.fill_rect(190,135,30,30,LCD.red)
        else :
            LCD.fill_rect(190,135,30,30,LCD.white)
            LCD.rect(190,135,30,30,LCD.red)
            
        if(keyY.value() == 0):
            LCD.fill_rect(190,195,30,30,LCD.red)
        else :
            LCD.fill_rect(190,195,30,30,LCD.white)
            LCD.rect(190,195,30,30,LCD.red)
            
        if(up.value() == 0):
            LCD.fill_rect(60,90,30,30,LCD.red)
        else :
            LCD.fill_rect(60,90,30,30,LCD.white)
            LCD.rect(60,90,30,30,LCD.red)
            
        if(dowm.value() == 0):
            LCD.fill_rect(60,180,30,30,LCD.red)
        else :
            LCD.fill_rect(60,180,30,30,LCD.white)
            LCD.rect(60,180,30,30,LCD.red)
            
        if(left.value() == 0):
            LCD.fill_rect(15,135,30,30,LCD.red)
        else :
            LCD.fill_rect(15,135,30,30,LCD.white)
            LCD.rect(15,135,30,30,LCD.red)
        
        if(right.value() == 0):
            LCD.fill_rect(105,135,30,30,LCD.red)
        else :
            LCD.fill_rect(105,135,30,30,LCD.white)
            LCD.rect(105,135,30,30,LCD.red)
        
        if(ctrl.value() == 0):
            LCD.fill_rect(60,135,30,30,LCD.red)
        else :
            LCD.fill_rect(60,135,30,30,LCD.white)
            LCD.rect(60,135,30,30,LCD.red)
                       
        LCD.show()
    time.sleep(1)
    LCD.fill(0xFFFF)