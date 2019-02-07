import board
import time
import neopixel
import random
from prgs.xmas import xmasFnc
from prgs.swim import swimFnc
from prgs.flashing import flashingFnc
from prgs.countdown import countdownFnc
from prgs.line import lineFnc
from prgs.morse import morseFnc
from prgs.split import splitFnc
from prgs.swipe import swipeFnc
from prgs.off import offFnc
from prgs.fade import fadeFnc
import os

pixel_pin = board.D21
num_pixels = 150
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

pixels.fill((0,0,0))
pixels.show()

def pickPrg(option):
	if option=="xmas":
		xmasFnc()
	elif option=="swim":
		swimFnc()
	elif option=="flashing":
		flashingFnc()
	elif "countdown" in option:
		optionSplit = option.split(" ")
		num = optionSplit[1]
		countdownFnc(num)
	elif option=="line":
		lineFnc()
	elif option=="split":
		splitFnc()
	elif option=="swipe":
		swipeFnc()
	elif "morse" in option:
		morseCode = option.split(" ")
		morseMsg = ""
		for x in range(1,len(morseCode)):
			morseMsg+=morseCode[x] + " "
		morseFnc(morseMsg)
	elif option=="off":
		offFnc()
	elif option=="fade":
		fadeFnc()
	elif option=="list":
		print("")
		os.system("ls prgs | sed -n 's/\.py$//p'")
		print("")
	else:
		print("Unknown command")

os.system("ls prgs | sed -n 's/\.py$//p'")
while True:
	option = input("Which function would you like to choose: ")
	pickPrg(option)