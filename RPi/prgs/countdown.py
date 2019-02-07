"""import board
import neopixel
import time
import sys
#
pixel_pin = board.D21
num_pixels = 150
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER)
"""
#
#pixels.fill((255,0,0))
#pixels.show()

def countdownFnc(args):
	if len(args)>1:
		wait = int(args)
	else:
		wait = int(input("Enter a time: "))

	if wait!=0:
		lightSplit = 150//wait
	else:
		return
	pointer = 149
	try:
		while wait>=0:
			for x in range(pointer,pointer-lightSplit-1,-1):
				pixels[x]=(0,0,255)
				pixels.show()
			wait -= 1
			pointer=pointer-lightSplit
			time.sleep(1)
	except KeyboardInterrupt:
		print("")
		pass