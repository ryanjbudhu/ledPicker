import board
import time
import neopixel
#import random
#
pixel_pin = board.D21
num_pixels = 150
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

def customFnc(colors):
	colorsplit = [int(colors[x:x+2],16) for x in range(0,len(colors),2)]
	pixels.fill((colorsplit[0],colorsplit[1],colorsplit[2]))
	pixels.show()