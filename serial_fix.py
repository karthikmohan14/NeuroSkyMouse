# print "Abriendo puerto"
import serial
ser = serial

try:
  ser = serial.Serial("com6", 9600, timeout = 1)
  serial_port = "Open"
  print("port available")

except serial.serialutil.SerialException:
  print("The port is at use")

  ser.close()
  ser.open()

while ser.read():
  print("Sending data") 

ser.setBreak(True)
time.sleep(0.2)

ser.sendBreak(duration = 0.02)
time.sleep(0.2)

ser.close()
time.sleep(0.2)
print("The port is closed") 

exit()