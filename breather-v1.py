# Mac Style Breathing Neopixel LEDs. I couldn't find a good python version of this.
# Basic code based on: https://wokwi.com/arduino/projects/305569065545499202
# The non-linear (gaussian?) light values are nicked from: 
# Adafruit's iCufflinks: https://github.com/adafruit/Adafruit_iCufflinks/blob/master/README.md


from neopixel import Neopixel
from time import sleep

## Setup
NUM_LEDS = 16
LED_PIN = 6 # The GPIO Pin in the pico
pixels = Neopixel(NUM_LEDS, 0, LED_PIN, "GRB")

breath = [
1, 1, 2, 3, 5, 8, 11, 15, 20, 25, 30, 36, 43, 49, 56, 64, 72, 80, 88, 97, 105, 114, 123, 132, 141, 150, 158, 167, 175, 183, 191, 199, 206, 212, 219, 225, 230, 235, 240, 244, 247, 250, 252, 253, 254, 255, 254, 253, 252, 250, 247, 244, 240, 235, 230, 225, 219, 212, 206, 199, 191, 183, 175, 167, 158, 150, 141, 132, 123, 114, 105, 97, 88, 80, 72, 64, 56, 49, 43, 36, 30, 25, 20, 15, 11, 8, 5, 3, 2, 1, 0
]

## Loop
while True:
  breath = breath[-1:] + breath[:-1]
  for i in range(len(breath)): # For each of the values in breath list (len counts the number of values)
    #print(breath[i]) # Use this to debug the light values
    pixels.brightness(breath[i]) # Set the pixel brightness to the breath value
    pixels.fill((255,255,255)) # Set the pixel colour - (255,255,255) is white
    pixels.show()
    sleep(0.05)