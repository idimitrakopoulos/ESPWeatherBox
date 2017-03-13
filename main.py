import time

from lib.bmp180.bmp180 import BMP180
from machine import I2C, Pin

bus =  I2C(scl=Pin(2), sda=Pin(0), freq=100000)
bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

while True:
    temp = bmp180.temperature
    p = bmp180.pressure
    altitude = bmp180.altitude
    print(temp, p, altitude)
    time.sleep(5)