import machine
import ssd1306
from lib.bmp180.bmp180 import BMP180
from machine import I2C, Pin

from lib.toolkit import scroll_down_show

# BMP180 init
bus =  I2C(scl=Pin(2), sda=Pin(0), freq=100000)
bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

# OLED init
i2c = machine.I2C(machine.Pin(4), machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

temperature = bmp180.temperature
pressure = bmp180.pressure
altitude = bmp180.altitude


oled.fill(0)
oled.text('Temp : ' + str(("%.1f" % temperature)) + "C", 0, 0)
oled.text('Press: ' + str(("%.2f" % (pressure / 100))) + "hPa", 0, 10)
oled.text('Alt  : ' + str(("%.2f" % altitude)) + "m", 0, 20)
oled.show()


for n in range(0,1000):
    scroll_down_show(oled, str(n))


