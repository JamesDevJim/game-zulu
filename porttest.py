import serial.tools.list_ports
import serial

a=serial.tools.list_ports.comports()
for w in a:
    print("Port:", w.device,"\tSerial#:", w.serial_number)
    if w.serial_number == '558383437333512132D0':
        ArduinoMegaPort = w.device

print('Arduino Mega Port', ArduinoMegaPort)