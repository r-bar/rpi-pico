import utime
import os
from machine import Pin

MESSAGE = 'I love you sam!'

# character timings
SLEEP = const(5)  # time between messages
MS = 0.001  # time in milliseconds
DOT = 50 * MS  # time to flash for a dot character
SEP = DOT # time between each flash
DASH = 3 * DOT # time to flash a dash character
SPACE = DASH # time between words
ONBOARD_LED = Pin(25, Pin.OUT)
OFFBOARD_LED = Pin(15, Pin.OUT)
BUZZER = Pin(14, Pin.OUT)
BUZZ_FREQ = 440

# mapping between dots dashes and spaces to led value and timing
DOTCHR = '.'
DASHCHR = '-'
SPACECHR = ' '
ACTIONS = {
    DOTCHR: (1, DOT),
    DASHCHR: (1, DASH),
    SPACECHR: (0, SPACE),
}

# mapping of string characters to dots and dashes
CODEX = {' ': SPACECHR}
with open('codex.txt') as f:
    for line in f:
        char, code = line.split()
        CODEX[char] = code


def encode(message: str):
    """Encode message into string of dots and dashes"""
    try:
        return ''.join(CODEX[c.upper()] for c in message)
    except KeyError as exc:
        raise ValueError('Message contains unencodable characters: %s' % exc)


def buzz(t=1, freq=BUZZ_FREQ, buzzer=BUZZER):
    start = utime.ticks_us()
    period = 1 / freq
    while True:
        buzzer.on()
        utime.sleep(period / 2)
        buzzer.off()
        utime.sleep(period / 2)
        elapsed = utime.ticks_us() - start
        if elapsed >= t * 10 ** 6:
            return


def send_char(char, dot_time=DOT, DASH_TIME=DASH, sep_time=SEP):
    state, timing = ACTIONS[char]

    ONBOARD_LED.value(state)
    OFFBOARD_LED.value(state)

    if state:
        buzz(timing)
    else:
        utime.sleep(timing)

    ONBOARD_LED.off()
    OFFBOARD_LED.off()

    utime.sleep(SEP)


def send(message: str):
    encoded = encode(message)
    print('sending:', message)
    print('encoded:', encoded)
    for char in encoded:
        send_char(char)


while True:
    send(MESSAGE)
    utime.sleep(SLEEP)
