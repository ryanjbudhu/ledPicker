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

def swipeFnc():
	wait = 0.03
	try:
		while True:
			for i in range(0,150):
				pixels[i] = (0,255,0)
				pixels.show()
				time.sleep(wait)
			for j in range(149,-1,-1):
				pixels[j] = (255,0,0)
				pixels.show()
				time.sleep(wait)
	except KeyboardInterrupt:
		print("")
		pass
	def rainbow_cycle(wait):
		for i in range(num_pixels):
			pixels[i] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
			pixels.show()
			time.sleep(wait)

	#rainbow_cycle(0.1)

	#pixels.show()
