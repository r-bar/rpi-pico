# Raspberry Pi Pico Projects

Collection of projects for learning about circuits and micro controllers with
the Raspberry Pi Pico.


## Requirements:

* rshell: A remote shell for pyboard
* ampy: Adafruit MicroPython tool
* minicom: A simple serial terminal program

User must be a member of the `uucp` group to read and write from `/dev/ttyACM0`.


## Environment Variables

```
export AMPY_PORT=/dev/ttyACM0
```


## Flashing a new binary

1. Hold down the reset button on the pico
2. Plug the pico into the computer
3. Wait for the drive to mount (takes about 3 seconds)
4. Copy a .u2f file to the drive
5. The board will automatically reset and disconnect


## Running a MicroPython program at board startup
Files must be loaded via `rshell` or `ampy put`, not by loading into the drive
when flashing the board.

Load board setup code into `boot.py` on the board. Execution appears to be time
boxed to ~2 seconds max.

Load main program into `main.py`. This will be executed immediately after `boot.py`.

The board does not appear to load new code after a soft reset, only a hard
reset.


## Helpful commands

Open rshell:
```
rshell --buffer-size=512 /dev/ttyACM0
```

Perform soft reset:
```
ampy reset
```

Perform hard reset:
```
ampy run --no-output reset.py
```

## References

* [MicroPython Reference](https://docs.micropython.org/en/latest/)
* [Pico Datasheet](https://datasheets.raspberrypi.org/pico/pico-datasheet.pdf)
* [Official Getting Started with Pico](https://datasheets.raspberrypi.org/pico/getting-started-with-pico.pdf)
* [rshell Guide](https://github.com/dhylands/rshell/blob/master/README.rst)
* [Pico Homepage](https://www.raspberrypi.org/documentation/pico/getting-started/)
* [MicroPython Wiki](https://github.com/micropython/micropython/wiki)
* [Pico Python SDK Guide](https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-python-sdk.pdf)
* [Pico C API Reference](https://raspberrypi.github.io/pico-sdk-doxygen/modules.html)
* [Picotool](https://github.com/raspberrypi/picotool): extra tools for working
  with the pico and its binaries
