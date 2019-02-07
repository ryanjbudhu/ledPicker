import board
import time
import neopixel
import random

pixel_pin = board.D21
num_pixels = 150
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)


#pixels.fill((255,0,0))
#pixels.show()

def flashingFnc():
	x = random.randrange(0,255)
	y = random.randrange(0,200)
	z = random.randrange(0,200)
	xascending = True
	yascending = False
	zascending = False
	wait = .00005
	try:
		while True:
			#for i in range(0,150):
			pixels.fill((x,y,z))
			pixels.show()
			if x <255 and xascending:
				x+=1
			elif x==255:
				x-=1
				xascending=False
			elif x==0:
				x+=1
				xascending=True
			else:
				x-=1
			if y <255 and yascending:
				y+=1
			elif y==255:
				y-=1
				yascending=False
			elif y==0:
				y+=1
				yascending=True
			else:
				y-=1
			if z <255 and zascending:
				z+=1
			elif z==255:
				z-=1
				zascending=False
			elif z==0:
				z+=1
				zascending=True
			else:
				z-=1
			time.sleep(wait)
	except KeyboardInterrupt:
		print("")
		pass
