import utime
from machine import Pin

INTERVAL = const(1)

led = Pin(25, Pin.OUT)

while True:
    led.toggle()
    utime.sleep(INTERVAL)
