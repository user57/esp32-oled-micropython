# Ordered from: https://www.aliexpress.com/item/32842966602.html?spm=a2g0s.9042311.0.0.37b94c4dKGgNt1
# Similar board - https://heltec.org/project/wifi-kit-32/
# More info: https://robotzero.one/heltec-wifi-kit-32/
# More info: https://www.minicontrollers.com/product/esp32-bluetooth-wifi-kit-oled-blue-0-96-inch-display-module-cp2102-32m-flash-3-3v-7v-internet-development-board-for-arduino/

# From https://github.com/micropython/micropython/tree/master/drivers/display
import ssd1306

from machine import Pin, I2C

# Onboard LED at Pin25
p25 = Pin(25, Pin.OUT)
p25.on()

# Text for display
line1: "Line1"
line2: "Line2"

# setup display

# After some searching (unknown source/facebook) p16/reset needs PULL_UP. 
p16 = Pin(16,Pin.IN,Pin.PULL_UP)

# SCL Pin 15
# SDA Pin 4
i2c = I2C(1, scl=Pin(15), sda=Pin(4), freq=400000)

display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.fill(0)
display.text(line1,0,0)
display.text(line2,0,10)

display.show()
