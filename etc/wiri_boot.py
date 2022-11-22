'''There are two files that are treated specially by the ESP8266 when it starts up: boot.py and main.py. 
The boot.py script is executed first (if it exists) and then once it completes the main.py script is executed. 
You can create these files yourself and populate them with the code that you want to run when the device starts up.'''
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

def do_connect(ssid, pwd):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, pwd)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


# This file is executed on every boot (including wake-boot from deepsleep)
import esp


esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()
# Attempt to connect to WiFi network
# do_connect('TP-Link_6B01', '09836716')