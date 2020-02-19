# Light test
import serial
import time
#ser = serial.Serial('/dev/ttyUSB0', 9600)
ser = serial.Serial('COM11', 9600)
time.sleep(2)


print("Welcome to ALA RgbStripSerial example")
print("A=[animation code] Set the animation. See https://github.com/bportaluri/ALA/blob/master/src/AlaLed.h")
print("B=[brightness]     Set the brightness [0-100]")
print("D=[duration]       Set the duration in milliseconds of the animation cycle")
print("C=[color]          Set the color (hexadecimal RGB representation ex. 0xE8A240)")
print("P=[palette]        Set the palette.")


# From Raspi to Arduino
ser.flush()
messageSend = "D=500"
messageSend = messageSend +'\n'
ser.write(messageSend.encode())
ser.flush()
print('Human Read Version: ',messageSend,'Arduino Version: ', messageSend.encode())

time.sleep(1)
ser.flush()
messageSend = "B=20"
messageSend = messageSend +'\n'
ser.write(messageSend.encode())
ser.flush()
print('Human Read Version: ',messageSend,'Arduino Version: ', messageSend.encode())

time.sleep(1)
ser.flush()
messageSend = "A=103"
messageSend = messageSend +'\n'
ser.write(messageSend.encode())
ser.flush()
print('Human Read Version: ',messageSend,'Arduino Version: ', messageSend.encode())





## Animations
#define ALA_ON 101
#define ALA_OFF 102
#define ALA_BLINK 103
#define ALA_BLINKALT 104
#define ALA_SPARKLE 105
#define ALA_SPARKLE2 106
#define ALA_STROBO 107

#define ALA_CYCLECOLORS 151

#define ALA_PIXELSHIFTRIGHT 201
#define ALA_PIXELSHIFTLEFT 202
#define ALA_PIXELBOUNCE 203
#define ALA_PIXELSMOOTHSHIFTRIGHT 211
#define ALA_PIXELSMOOTHSHIFTLEFT 212
#define ALA_PIXELSMOOTHBOUNCE 213
#define ALA_COMET 221
#define ALA_COMETCOL 222
#define ALA_BARSHIFTRIGHT 231
#define ALA_BARSHIFTLEFT 232
#define ALA_MOVINGBARS 241
#define ALA_MOVINGGRADIENT 242
#define ALA_LARSONSCANNER 251
#define ALA_LARSONSCANNER2 252

#define ALA_FADEIN 301
#define ALA_FADEOUT 302
#define ALA_FADEINOUT 303
#define ALA_GLOW 304
#define ALA_PLASMA 305

#define ALA_FADECOLORS 351
#define ALA_FADECOLORSLOOP 352
#define ALA_PIXELSFADECOLORS 353
#define ALA_FLAME 354

#define ALA_FIRE 501
#define ALA_BOUNCINGBALLS 502
#define ALA_BUBBLES 503

#define ALA_ENDSEQ 0
#define ALA_STOPSEQ 1