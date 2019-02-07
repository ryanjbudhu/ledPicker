import board
import time
import neopixel
##import random
pixel_pin = board.D21
num_pixels = 150 
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

def offFnc():
	pixels.fill((0,0,0))
	pixels.show()
