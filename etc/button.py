

from machine import Pin

print("welcome to button")

# define pin 13 as an input and activate an internal Pull-up resistor:
led = Pin(32, Pin.OUT)
button = Pin(25, Pin.IN, Pin.PULL_UP)

while True:
  
  logic_state = button.value()
  if logic_state == True:     # if pressed the push_button
      led.value(1)             # led will turn ON
  else:                       # if push_button not pressed
      led.value(0)             # led will turn OFF