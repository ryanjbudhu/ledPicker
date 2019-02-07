import board
import neopixel
import time
#
pixel_pin = board.D21
num_pixels = 150
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER)
#
#pixels.fill((0,0,255))

def swimFnc():
	lights = {"blead":7,"lead":6,"mid1":5,"mid2":4,"green":3,"last1":2,"last2":1,"end":0}
	#lights = {"blead":2,"lone":1,"end":0}
	wait = .005
	ascending = [x for x in lights]
	try:
		while True:
			for x in lights:
				if x=="end" or x=="blead" or x=="green":
					pixels[lights[x]]=(0,0,255)
				elif x=="lead":
					pixels[lights[x]]=(0,255,0)
				elif x=="last2":
					pixels[lights[x]]=(255,0,0)
				else:
					pixels[lights[x]]=(255,153,11)
				#if lights[x]==149:
					#lights[x]=0
				if x in ascending:
					lights[x]+=1
					if lights[x]==149:
						ascending.remove(x)
				else:
					lights[x]-=1
					if lights[x]==0:
						ascending.append(x)
			'''	elif lights[x]==0:
					ascending=True
				if ascending:
					lights[x]+=1
				else:
					lights[x]-=1
			'''
			pixels.show()
			time.sleep(wait)
	except KeyboardInterrupt:
		print("")
		pass
