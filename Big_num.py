import time
import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20


def zero(x):
    lcd.move_to(x, 0)
    lcd.putstr('\x04\x01\x01\x03')
    lcd.move_to(x, 1)
    lcd.putstr('\x01\x00\x00\x01')
    lcd.move_to(x, 2)
    lcd.putstr('\x01\x00\x00\x01')
    lcd.move_to(x, 3)
    lcd.putstr('\x05\x01\x01\x06')

def one(x):
    lcd.move_to(x, 0)
    lcd.putstr('\x00\x04\x01\x00')
    lcd.move_to(x, 1)
    lcd.putstr('\x00\x00\x01\x00')
    lcd.move_to(x, 2)
    lcd.putstr('\x00\x00\x01\x00')
    lcd.move_to(x, 3)
    lcd.putstr('\x00\x07\x01\x07')

def two(x):
    lcd.move_to(x, 0)
    lcd.putstr('\x02\x02\x02\x03')
    lcd.move_to(x, 1)
    lcd.putstr('\x00\x00\x00\x01')
    lcd.move_to(x, 2)
    lcd.putstr('\x04\x02\x02\x02')
    lcd.move_to(x, 3)
    lcd.putstr('\x01\x07\x07\x07')

def three(x):
    lcd.move_to(x, 0)
    lcd.putstr('\x04\x01\x01\x03')
    lcd.move_to(x, 1)
    lcd.putstr('\x00\x07\x07\x01')
    lcd.move_to(x, 2)
    lcd.putstr('\x00\x00\x00\x01')
    lcd.move_to(x, 3)
    lcd.putstr('\x05\x01\x01\x06')
    
def four(x):
    lcd.move_to(x, 0)
    lcd.putstr('\x01\x00\x00\x01')
    lcd.move_to(x, 1)
    lcd.putstr('\x01\x07\x07\x01')
    lcd.move_to(x, 2)
    lcd.putstr('\x00\x00\x00\x01')
    lcd.move_to(x, 3)
    lcd.putstr('\x00\x00\x00\x01')

def five(x):
    lcd.move_to(x, 0)
    lcd.putstr('\x01\x02\x02\x02')
    lcd.move_to(x, 1)
    lcd.putstr('\x01\x07\x07\x07')
    lcd.move_to(x, 2)
    lcd.putstr('\x00\x00\x00\x01')
    lcd.move_to(x, 3)
    lcd.putstr('\x07\x07\x07\x06')

def six(x):
    lcd.move_to(x, 0)
    lcd.putstr('\x04\x02\x02\x02')
    lcd.move_to(x, 1)
    lcd.putstr('\x01\x07\x07\x07')
    lcd.move_to(x, 2)
    lcd.putstr('\x01\x00\x00\x01')
    lcd.move_to(x, 3)
    lcd.putstr('\x05\x07\x07\x06')

def seven(x):
    lcd.move_to(x, 0)
    lcd.putstr('\x02\x02\x02\x01')
    lcd.move_to(x, 1)
    lcd.putstr('\x00\x00\x00\x06')
    lcd.move_to(x, 2)
    lcd.putstr('\x00\x00\x06\x00')
    lcd.move_to(x, 3)
    lcd.putstr('\x00\x01\x00\x00')

def eight(x):
    lcd.move_to(x, 0)
    lcd.putstr('\x04\x01\x01\x03')
    lcd.move_to(x, 1)
    lcd.putstr('\x01\x07\x07\x01')
    lcd.move_to(x, 2)
    lcd.putstr('\x01\x00\x00\x01')
    lcd.move_to(x, 3)
    lcd.putstr('\x05\x01\x01\x06')

def nine(x):
    lcd.move_to(x, 0)
    lcd.putstr('\x04\x02\x02\x03')
    lcd.move_to(x, 1)
    lcd.putstr('\x05\x07\x07\x01')
    lcd.move_to(x, 2)
    lcd.putstr('\x00\x00\x00\x01')
    lcd.move_to(x, 3)
    lcd.putstr('\x00\x00\x00\x01')
    
def load_Num_Bits():
    lcd.custom_char(0, (0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000))## bit0                                 
    lcd.custom_char(1, (0b11111,0b11111,0b11111,0b11111,0b11111,0b11111,0b11111,0b11111))## bit1
    lcd.custom_char(2, (0b11111,0b11111,0b11111,0b11111,0b11111,0b00000,0b00000,0b00000))## bit2
    lcd.custom_char(3, (0b00000,0b11000,0b11100,0b11110,0b11110,0b11111,0b11111,0b11111))## bit3                                         
    lcd.custom_char(4, (0b00000,0b00011,0b00111,0b01111,0b01111,0b11111,0b11111,0b11111))## bit4                                  
    lcd.custom_char(5, (0b11111,0b11111,0b11111,0b01111,0b01111,0b00111,0b00011,0b00000))## bit5                                        
    lcd.custom_char(6, (0b11111,0b11111,0b11111,0b11110,0b11110,0b11100,0b11000,0b00000))## bit6
    lcd.custom_char(7, (0b00000,0b00000,0b00000,0b11111,0b11111,0b11111,0b11111,0b11111))## bit7
           
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

load_Num_Bits()

## test code
one(0)
two(5)
three(11)
four(16)
