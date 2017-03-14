import time

import ssd1306
from lib.bmp180.bmp180 import BMP180
from machine import I2C, Pin

# BMP180 init
bus =  I2C(scl=Pin(2), sda=Pin(0), freq=100000)
bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

# OLED init
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

while True:
    temp = bmp180.temperature
    p = bmp180.pressure
    altitude = bmp180.altitude


    oled.fill(0)
    oled.text('illuminOS v0.0.2- esp', 0, 0)
    oled.text('Temp: ' + str(("%.1f" % temp)), 1, 0)
    # oled.text('Humidity: ' + str(d.humidity()), 2, 0)
    oled.show()

    print(("%.1f" % temp), ("%.2f" % p), ("%.2f" % altitude))
    time.sleep(5)