import board
import time
import neopixel
#import random
#
pixel_pin = board.D21
num_pixels = 150
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

#
#pixels.fill((255,0,0))
#pixels.show()

def splitFnc():
	wait=.005
	r = 0
	g = 255
	b = 0
	try:
		while True:
			#print(r,g,b)
			if b==255:
				b=0
				r=255
			elif r==255:
				r=0
				g=255
			elif g==255:
				g=0
				b=255
			up = 75
			down = 73
			pixels[74] = (r,g,b)
			pixels.show()
			while down>=0:
				pixels[up]=(r,g,b)
				pixels[down]=(r,g,b)
				up+=1
				down-=1
				pixels.show()
				time.sleep(wait)
	except KeyboardInterrupt:
		print("")
		pass
