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
        
        def buttonAny(self):
            key1 = PIN_ONE.read()
            key2 = PIN_TWO.read()
            key3 = PIN_THREE.read()
            key4 = PIN_LEFT.read()
            key5 = PIN_RIGHT.read()
            key6 = PIN_UP.read()
            key7 = PIN_DOWN.read()
            key8 = PIN_BACK.read()
            keys = [key1, key2, key3, key4, key5, key6, key7, key8]
            
            if all(keys):
                return False
            return True

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
        
        def buttonAny(self):            
            keys = pygame.key.get_pressed()
            if any(keys):
                return True
            return False
    # Debounce to make sure we don't send two button pushed
    time.sleep(0.3)

# Set up a class to turn on/off the LEDs. If LEDs are not available then ignore them.       
class Light:
    def __init__(self):
        self.pressed = [0,]*1000
        self.released = [0,]*1000          

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
        
        # TODO: Make all lights into an array to make code cleaner. 
        def all(self, state):           
            if state == 1:
                return (PIN_LED_B1.write(1), PIN_LED_B2.write(1), PIN_LED1.write(1), PIN_LED2.write(1), PIN_LED3.write(1), PIN_LED4.write(1), PIN_LED5.write(1))
            if state == 0:
                return (PIN_LED_B1.write(0), PIN_LED_B2.write(0), PIN_LED1.write(0), PIN_LED2.write(0), PIN_LED3.write(0), PIN_LED4.write(0), PIN_LED5.write(0))  
            if state == None:
                pass

        # TODO: ALLOW LIGHTS to blink but not thread block.    
        def blink(self,rate,times):
            for i in range(times):
                (PIN_LED_B1.write(1), PIN_LED_B2.write(1), PIN_LED1.write(1), PIN_LED2.write(1), PIN_LED3.write(1), PIN_LED4.write(1), PIN_LED5.write(1))
                time.sleep(rate)
                (PIN_LED_B1.write(0), PIN_LED_B2.write(0), PIN_LED1.write(0), PIN_LED2.write(0), PIN_LED3.write(0), PIN_LED4.write(0), PIN_LED5.write(0))  
                time.sleep(rate)  

        # TODO: Create a method that sequences through all lights
        # Def sequence(self, rate, times):
        #   for i in range(times):
        #       for i in range LIGHT:
        #           # LIGHT[i] ON
        #           # time.sleep(rate) 
        #           # LIGHT[i] OFF
        #           # time.sleep(rate)
        #                      

    # TODO: If neccessary, create an list of simulated lights so tester w/o arduino board can see what is lit and what is not
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
        def all(self, state):
            pass
        def blink(self,rate,times):
            pass            
