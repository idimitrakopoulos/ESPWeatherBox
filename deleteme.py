import dht, ssd1306
import machine, time
d = dht.DHT11(machine.Pin(10))

i2c = machine.I2C(machine.Pin(4), machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

while True:
    d.measure()
    oled.fill(0)
    oled.text('illuminOS v0.0.2- esp', 0, 0)
    oled.text('Temp: ' + str(d.temperature()), 0, 10)
    oled.text('Humidity: ' + str(d.humidity()), 0, 20)
    oled.show()
    time.sleep(10)
