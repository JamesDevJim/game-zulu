import serial
import time

print('-------------------------------------------------------------------------------------\n''Test Light Strip \n'+'')

try:
    #arduino2 = serial.Serial('/dev/ttyUSB0', 9600)
    arduino2 = serial.Serial('COM11', 9600)
    time.sleep(1.5)
    print('Using Arduino')
except:
    pass
# Obtained structure from: https://github.com/bportaluri/AlaWeb/blob/master/AlaWeb.py
def arduino2_get_resp(s):
    time.sleep(.1)
    while (s.in_waiting > 0):
        print(s.readline().decode(), end="")

def arduino2_send_cmd(s):
    arduino2.flush()
    s = s+'\n'
    arduino2.write(s.encode())
    arduino2_get_resp(arduino2)
    time.sleep(.1)
    arduino2.flush()

def strip(animation, brightness=None, duration=None , color=None, palette=None):
    if animation is not None:
        arduino2_send_cmd(animation)    
    if brightness is not None:   
        arduino2_send_cmd(brightness)
    if duration is not None:
        arduino2_send_cmd(duration)
    if duration is not None:
        arduino2_send_cmd(duration)
    if color is not None:      
        arduino2_send_cmd(color)
    if palette is not None:      
        arduino2_send_cmd(palette)

##### TESTS #####

# # On test
# print('Light Test: ON')
# arduino2_send_cmd('A=101')
# time.sleep(2)
# arduino2_send_cmd('A=102')
# time.sleep(2)

# # Blink test maybe for alarm
# print('Light Test: BLINK')
# arduino2_send_cmd('D=500')
# arduino2_send_cmd('A=103')
# time.sleep(2)
# arduino2_send_cmd('A=102')
# time.sleep(2)

# # Lars Scanner test
# print('Light Test: SCANNER')
# arduino2_send_cmd('D=1000')
# arduino2_send_cmd('P=5')
# arduino2_send_cmd('A=251')
# time.sleep(2)
# arduino2_send_cmd('A=102')
# time.sleep(2)

# # Battle test for Xray
# print('Light Test: BATTLE')
# arduino2_send_cmd('D=2000')
# arduino2_send_cmd('C=0xFF0000')
# arduino2_send_cmd('A=103')
# time.sleep(4)
# arduino2_send_cmd('A=102')
# time.sleep(2)

# # Plasma for Whiskey
# print('Light Test: PLASMA')
# arduino2_send_cmd('A=305')
# arduino2_send_cmd('P=5')
# time.sleep(2)
# arduino2_send_cmd('A=102')
# time.sleep(2)

# Spark test 
print('Light Test: SPARK')
# arduino2_send_cmd('D=200')
# arduino2_send_cmd('P=0')
# arduino2_send_cmd('A=107')
# time.sleep(2)
# arduino2_send_cmd('A=102')
# time.sleep(2)


# strip('A=107','B=100','D=200',None,'P=0')
# time.sleep(4)

# PLASMA
print('Light Test: PLASMA')
strip('A=305','B=80','D=3000',None,'P=5')
time.sleep(4)

# SPARK
print('Light Test: SPARK')
strip('A=251','B=100','D=1000',None,'P=0')
time.sleep(4)

# GAMEPLAY SPACESHIP
print('Light Test: GAMEPLAY SPACESHIP')
strip('A=251','B=70','D=1000',None,'P=5')
time.sleep(4)

# GAMEPLAY BLUE
print('Light Test: GAMEPLAY')
strip('A=101',None,None,'C=0x0000FF','P=0')
time.sleep(4)

# GAMEPLAY DARK BLUE
print('Light Test: GAMEPLAY')
strip('A=101',None,None,'C=0x000080','P=0')
time.sleep(4)


# SUCCESS
print('Light Test: Success')
strip('A=303',None,'D=2000','C=0x00FF00','P=0')
time.sleep(4)

# FAIL
print('Light Test: Fail')
strip('A=303',None,'D=2000','C=0xFF0000','P=0')
time.sleep(4)

# ON
print('Light Test: On')
strip('A=101')
time.sleep(4)

# OFF
print('Light Test: Off')
strip('A=102')
time.sleep(4)

# On test
# print('Light Test: ON FUNCTION TEST')
# strip('A=305',None,'D=500',None,'P=5')
# time.sleep(6)
# strip('A=102')
# time.sleep(2)

# print("Welcome to ALA RgbStripSerial example")
# print("A=[animation code] Set the animation. See https://github.com/bportaluri/ALA/blob/master/src/AlaLed.h")
# print("B=[brightness]     Set the brightness [0-100]")
# print("D=[duration]       Set the duration in milliseconds of the animation cycle")
# print("C=[color]          Set the color (hexadecimal RGB representation ex. 0xE8A240)")
# print("P=[palette]        Set the palette.")


##### ANIMATIONS #####
    #ON 101
    #OFF 102
    #BLINK 103
    #BLINKALT 104
    #SPARKLE 105
    #SPARKLE2 106
    #STROBO 107

    #CYCLECOLORS 151

    #PIXELSHIFTRIGHT 201
    #PIXELSHIFTLEFT 202
    #PIXELBOUNCE 203
    #PIXELSMOOTHSHIFTRIGHT 211
    #PIXELSMOOTHSHIFTLEFT 212
    #PIXELSMOOTHBOUNCE 213
    #COMET 221
    #COMETCOL 222
    #BARSHIFTRIGHT 231
    #BARSHIFTLEFT 232
    #MOVINGBARS 241
    #MOVINGGRADIENT 242
    #LARSONSCANNER 251
    #LARSONSCANNER2 252

    #FADEIN 301
    #FADEOUT 302
    #FADEINOUT 303
    #GLOW 304
    #PLASMA 305

    #FADECOLORS 351
    #FADECOLORSLOOP 352
    #PIXELSFADECOLORS 353
    #FLAME 354

    #FIRE 501
    #BOUNCINGBALLS 502
    #BUBBLES 503

    # ENDSEQ 0
    # STOPSEQ 1


##### COLORS #####
    # Red #FF0000
    # Yellow #FFFF00
    # Green #00FF00
    # Green D #008000
    # Blue #0000FF
    # Blue D #000080
    # Fushia #FF00FF

##### PALATE #####
    # 0 - White
    # 1
    # 2
    # 3 - Rambow?
    # 4
    # 5 - Fire

print('-------------------------------------------------------------------------------------\n''Test Light Strip Complete \n'+'')