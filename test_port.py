import serial
import serial.tools.list_ports

print(
    "-------------------------------------------------------------------------------------\n"
    "Test Ports \n" + ""
)

a = serial.tools.list_ports.comports()

ArduinoMegaPort = "None"
ArduinoNanoPort = "None"
ArduinoNano2Port = "None"

for w in a:
    print("Port:", w.device, "\tSerial#:", w.serial_number)
    if w.serial_number == "558383437333512132D0":
        ArduinoMegaPort = w.device

    if w.serial_number == "5":
        ArduinoNanoPort = w.device

print("Arduino Mega Port: ", ArduinoMegaPort)
print("Arduino Nano Port: ", ArduinoNanoPort)
print("Arduino Nano2 Port: ", ArduinoNano2Port)

print(
    "\n"
    "Test Ports Complete\n"
    "-------------------------------------------------------------------------------------"
)
