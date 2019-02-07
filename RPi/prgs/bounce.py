import board
import time
import neopixel
import math

pixel_pin = board.D21
num_pixels = 150
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=True, pixel_order=ORDER)
#pixels.fill((0,0,0))
wait = .005
colors = {"red":(255,0,0),"green":(0,255,0),"blue":(0,0,255),"yellow":(255,255,0),"cyan":(0,255,255),"magenta":(255,0,255)}


def bounceFnc():
	try:
		while True:
			for realcolor in colors:
				pcolor = [0,0,0]
				multiplier = .02
				while multiplier<1.02:
					for p in range(0,3):
						if pcolor[p]==0:
							pcolor[p]=math.floor(colors[realcolor][p]*.02)
						elif pcolor[p]<colors[realcolor][p]:
							pcolor[p]=math.floor(colors[realcolor][p]*multiplier)
					pixels.fill(tuple(pcolor))
					multiplier+=.02
					time.sleep(wait)
				multiplier = 1
				while not all([v==0 for v in pcolor]):
					for p in range(0,3):
						if pcolor[p]!=0:
							pcolor[p]=math.floor(colors[realcolor][p]*multiplier)
						if(multiplier>.02):
							multiplier-=.02
						else:
							multiplier=0
					pixels.fill(tuple(pcolor))
					time.sleep(wait)
	except KeyboardInterrupt:
			print("")
			pass