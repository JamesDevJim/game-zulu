import serial.tools.list_ports
import serial

a=serial.tools.list_ports.comports()

ArduinoMegaPort = 'None'
ArduinoNanoPort = 'None'
ArduinoNano2Port = 'None'

# comment
for w in a:
    print("Port:", w.device,"\tSerial#:", w.serial_number, w.hwid, w.vid, w.name)
    if w.serial_number == '558383437333512132D0':
        ArduinoMegaPort = w.device

    if w.serial_number == '5':
        ArduinoNanoPort = w.device

print('Arduino Mega Port: ', ArduinoMegaPort)
print('Arduino Nano Port: ', ArduinoNanoPort)
print('Arduino Nano2 Port: ', ArduinoNano2Port)