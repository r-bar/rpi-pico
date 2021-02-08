from machine import Pin


ONBOARD_LED = Pin(25, Pin.OUT)
OFFBOARD_LED = Pin(15, Pin.OUT)
BUZZER = Pin(14, Pin.OUT)


BUZZER.off()
ONBOARD_LED.off()
OFFBOARD_LED.off()
