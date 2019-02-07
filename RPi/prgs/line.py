import board
import neopixel
import time
#
pixel_pin = board.D21
num_pixels = 150
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER)

#
#pixels.fill((255,0,0))
#pixels.show()

def lineFnc():
	wait = .05
	redStart = 0
	greenStart = 1
	blueStart = 2
	try:
		while True:
			for red in range(redStart,150,3):
				pixels[red] = (255,0,0)
			for green in range(greenStart,150,3):
				pixels[green] = (0,255,0)
			for blue in range(blueStart,150,3):
				pixels[blue] = (0,0,255)
			pixels.show()
			time.sleep(wait)
			if redStart <2:
				redStart+=1
			else:
				redStart = 0
			if greenStart <2:
				greenStart+=1
			else:
				greenStart = 0
			if blueStart <2:
				blueStart+=1
			else:
				blueStart = 0
	except KeyboardInterrupt:
		print("")
		pass
