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

def fadeFnc():
	wait=.0005
	r = 0
	g = 250
	b = 0
	try:
		while True:
			#print(r,g,b)
			if r>0 and b==0:
				r-=10
				g+=10
			if g>0 and r==0:
				g-=10
				b+=10
			if b>0 and g==0:
				b-=10
				r+=10
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
