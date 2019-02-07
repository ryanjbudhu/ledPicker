import board
import neopixel
import time
import sys

pixel_pin = board.D21
num_pixels = 150
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER)

encodeMorse= {
	"A": "•-",
	"B": "-•••",
	"C": "-•-•",
	"D": "-••",
	"E": "•",
	"F": "••–•",
	"G": "--•",
	"H": "••••",
	"I": "••",
	"J": "•---",
	"K": "-•-",
	"L": "•-••",
	"M": "––",
	"N": "-•",
	"O": "---",
	"P": "•--•",
	"Q": "--•-",
	"R": "•-•",
	"S": "•••",
	"T": "-",
	"U": "••-",
	"V": "•••-",
	"W": "•--",
	"X": "-••-",
	"Y": "-•--",
	"Z": "--••",
	"1": "•----",
	"2": "••---",
	"3": "•••--",
	"4": "••••-",
	"5": "•••••",
	"6": "-••••",
	"7": "--•••",
	"8": "---••",
	"9": "----•",
	"0": "-----",
	" ": "••--"
}
def encoder(unencoded):
	unencoded = unencoded.upper()
	encoded = []
	for letter in unencoded:
		encoded.append(encodeMorse[letter])
	return encoded
def showPixels(revEncode):	#Convert to pixels
	pixels.fill((0,0,0))
	wait = .05
	light = {}
	dotCount = 0
	dashCount = 100
	spaceCount = 200
	
	for letter in revEncode:
		for piece in letter:
			if piece == "•":
				light[dotCount] = 0
				dotCount +=1
			else:
				light[dashCount] = 0
				dashCount +=1
			for x in light:
				if light[x]<149:
					if x<100:# if its a -
						pixels[light[x]] = (0,0,255)
						light[x]+=1
					elif x >99 and x<200:# if its a •
						pixels[light[x]] = (0,255,0)
						light[x]+=1
					elif x >199:# if its a space
						pixels[light[x]] = (0,0,0)
						light[x]+=1
				else:
					#light.pop(x)
					light[x] = 0
			pixels.show()
			time.sleep(wait)
		
		light[spaceCount] = 0
		spaceCount += 1
		for x in light:
			if light[x]<149:
				if x<100:# if its a -
					pixels[light[x]] = (0,0,255)
					light[x]+=1
				elif x >99 and x<200:# if its a •
					pixels[light[x]] = (0,255,0)
					light[x]+=1
				elif x >199:# if its a space
					pixels[light[x]] = (0,0,0)
					light[x]+=1
			else:
				#light.pop(x)
				light[x] = 0
	pixels.show()
	#for x in light:
		#print(str(x)+":"+str(light[x]))
	pixels.show()
	try:
		while len(light)>0:
			for x in light.keys():
				if light[x]<149:
					if x<100:
						pixels[light[x]] = (0,0,255)
						light[x]+=1
					elif x>99 and x<200:
						pixels[light[x]] = (0,255,0)
						light[x]+=1
					elif x>199:
						pixels[light[x]] = (0,0,0)
						light[x]+=1
				else:
					#light.pop(x)
					light[x] = 0
			pixels.show()
			time.sleep(wait)
	except KeyboardInterrupt:
		pass

def morseFnc(uncoded):
	try:
			encoded = encoder(uncoded)
			#encoded = encoded.rstrip()
			revEncode = [reversed(x) for x in encoded]
			#revEncode = encoded[::-1]
			#revEncode = encoded.split(" ")
			
			showPixels(revEncode)
	except KeyboardInterrupt:
		print("")
		pass

#wait = .05
#argLength = len(sys.argv)
#try:
#	while True:
#		if argLength > 1:
#			if argLength > 2:
#				uncodedList = sys.argv
#				uncoded = ""
#				for arg in range(1,len(uncodedList)):
#					uncoded += uncodedList[arg] + " "
#			else:
#				uncoded = sys.argv[1]
#			argLength = 0
#			uncoded = uncoded.rstrip()
#		else:
#			uncoded = input("Enter word to be coded: ")
#		if not uncoded.replace(" ","").isalnum():
#			break
#		encoded = encoder(uncoded)
#		encoded = encoded.rstrip()
#		revEncode = encoded[::-1]
#		revEncode = encoded.split(" ")
#		
#		showPixels(revEncode)
#except KeyboardInterrupt:
#	print("")
#	pass
