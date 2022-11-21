from machine import Pin
from time import sleep

led = Pin(32, Pin.OUT)
button = Pin(25, Pin.IN, Pin.PULL_UP)




for i in range(10):
  led.value(not led.value())
  sleep(0.5)
  i += 1
  print(i)