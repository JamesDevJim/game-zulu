import pygame
import time
from pyfirmata import ArduinoMega, util

clock = pygame.time.Clock()
useArduino = True

# Try to connect to the arduino board. If it fails, then we will use the keyboard.
try:
    arduino = ArduinoMega('COM7')
    time.sleep(0.2)  
    iterator = util.Iterator(arduino)
    iterator.start()
    time.sleep(0.2)  

    # Define all input pins
    PIN_ONE = arduino.get_pin('d:37:i')
    PIN_TWO = arduino.get_pin('d:36:i')
    PIN_THREE = arduino.get_pin('d:35:i')
    PIN_LEFT = arduino.get_pin('d:32:i')
    PIN_RIGHT = arduino.get_pin('d:31:i')
    PIN_UP = arduino.get_pin('d:34:i')
    PIN_DOWN = arduino.get_pin('d:33:i')
    PIN_BACK = arduino.get_pin('d:30:i')

    #Define all lights
    PIN_LED_B1 = arduino.get_pin('d:11:p')
    PIN_LED_B2 = arduino.get_pin('d:10:p')
    PIN_LED1 = arduino.get_pin('d:3:p')
    PIN_LED2 = arduino.get_pin('d:2:p')
    PIN_LED3 = arduino.get_pin('d:5:p')
    PIN_LED4 = arduino.get_pin('d:4:p')
    PIN_LED5 = arduino.get_pin('d:13:p')

except:
    useArduino = False
    print('Button box failed to connect.')

# Set up a class to read all the inputs on the box. If box is not availabled then use the keyboard.
class Control:
    def __init__(self):
        self.pressed = [0,]*1000
        self.released = [0,]*1000    
        #TODO: Create an object to detect return true is ANY button is pushed.
            
    if useArduino:
        def one(self):
            keys = PIN_ONE.read()
            if not keys:
                return True
            return False    

        def two(self):
            keys = PIN_TWO.read()
            if not keys:
                return True
            return False
        
        def three(self):
            keys = PIN_THREE.read()
            if not keys:
                return True
            return False    
    
        def left(self):
            keys = PIN_LEFT.read()
            if not keys:
                return True
            return False   

        def right(self):
            keys = PIN_RIGHT.read()
            if not keys:
                return True
            return False   

        def up(self):
            keys = PIN_UP.read()
            if not keys:
                return True
            return False   

        def down(self):
            keys = PIN_DOWN.read()
            if not keys:
                return True
            return False   

        def back(self):
            keys = PIN_BACK.read()
            if not keys:
                return True
            return False   

    if not useArduino:
        def one(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                return True
            return False         
       
        def two(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_2]:
                return True
            return False    
       
        def three(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_3]:
                return True
            return False  
            
        def left(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                return True
            return False

        def right(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                return True
            return False

        def up(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                return True
            return False

        def down(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                return True
            return False

        def back(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                return True
            return False
        

# Set up a class to turn on/off the LEDs. If LEDs are not available then ignore them.       
class Light:
    def __init__(self):
        self.pressed = [0,]*1000
        self.released = [0,]*1000          
        
        #TODO: Create an object to turn on ALL lights here....
        #TODO: Create an object to blink and trail sequence lights here...

    lightArrayOn = [PIN_LED_B1.write(1), PIN_LED_B2.write(1), PIN_LED1.write(1), PIN_LED2.write(1), PIN_LED3.write(1), PIN_LED4.write(1), PIN_LED5.write(1)]
    lightArrayOff = [PIN_LED_B1.write(0), PIN_LED_B2.write(0), PIN_LED1.write(0), PIN_LED2.write(0), PIN_LED3.write(0), PIN_LED4.write(0), PIN_LED5.write(0)]

    if useArduino:
        def buttonOne(self, state):
            if state == 1:
                PIN_LED_B1.write(1)
            if state == 0:
                PIN_LED_B1.write(0)   

        def buttonTwo(self, state):
            if state == 1:
                return PIN_LED_B2.write(1)
            if state == 0:
                return PIN_LED_B2.write(0)   
        
        def LED1(self, state):
            if state == 1:
                return PIN_LED1.write(1)
            if state == 0:
                return PIN_LED1.write(0)   
        
        def LED2(self, state):
            if state == 1:
                return PIN_LED2.write(1)
            if state == 0:
                return PIN_LED2.write(0)  

        def LED3(self, state):
            if state == 1:
                return PIN_LED3.write(1)
            if state == 0:
                return PIN_LED3.write(0)  

        def LED4(self, state):
            if state == 1:
                return PIN_LED4.write(1)
            if state == 0:
                return PIN_LED4.write(0)  

        def LED5(self, state):
            if state == 1:
                return PIN_LED5.write(1)
            if state == 0:
                return PIN_LED5.write(0)
        
        def ALL(self, state):
            if state == 1:
                return (PIN_LED_B1.write(1), PIN_LED_B2.write(1), PIN_LED1.write(1), PIN_LED2.write(1), PIN_LED3.write(1), PIN_LED4.write(1), PIN_LED5.write(1))  
            if state == 0:
                return (PIN_LED_B1.write(0), PIN_LED_B2.write(0), PIN_LED1.write(0), PIN_LED2.write(0), PIN_LED3.write(0), PIN_LED4.write(0), PIN_LED5.write(0))
            if state == 3:
                for i in range(4):
                    (PIN_LED_B1.write(1), PIN_LED_B2.write(1), PIN_LED1.write(1), PIN_LED2.write(1), PIN_LED3.write(1), PIN_LED4.write(1), PIN_LED5.write(1))
                    time.sleep(0.2)
                    (PIN_LED_B1.write(0), PIN_LED_B2.write(0), PIN_LED1.write(0), PIN_LED2.write(0), PIN_LED3.write(0), PIN_LED4.write(0), PIN_LED5.write(0))  
                    time.sleep(0.2)



    if not useArduino:   
        def buttonOne(self, state):
            pass
        def buttonTwo(self, state):
            pass    
        def LED1(self, state):
            pass      
        def LED2(self, state):
            pass
        def LED3(self, state):
            pass 
        def LED4(self, state):
            pass 
        def LED5(self, state):
            pass 
        def ALL(self, state):
            pass
