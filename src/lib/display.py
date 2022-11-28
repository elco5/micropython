# Complete project details at https://RandomNerdTutorials.com
# https://randomnerdtutorials.com/micropython-oled-display-esp32-esp8266/


from machine import Pin, SoftI2C
from lib import ssd1306
from time import sleep



class Display:

    
    def __init__(self):
        
        # ESP32 Pin assignment 
        i2c = SoftI2C(scl=Pin(22), sda=Pin(21))


        oled_width = 128
        oled_height = 64
        oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

    oled.text('Hello, World 1!', 0, 0)
    oled.text('Hello, World 2!', 0, 10)
    oled.text('Hello, World 3!', 0, 20)
            
    oled.show()