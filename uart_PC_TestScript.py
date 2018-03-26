import time, threading, serial, os

mode = 'w'

stop = 0
eingabe = ''
TickCounter = 0
PreAmbel = '0123456789'
Wert0 = 0
Wert1 = 0
Wert2 = 0
Wert3 = 0
Wert4 = 0
Wert5 = 0
Wert6 = 0
Wert7 = 0
Wert8 = 0
Wert9 = 0

ser = serial.Serial(
	port='/dev/ttyUSB0',
	baudrate=115200,
	parity=serial.PARITY_NONE,
	stopbits=1,
	bytesize=8
)
ser.close()
ser.open()
ser.isOpen()

os.system('cls')
print '  Tasten Befehle:'
print '  --------------------'
print '  x -> Programm beenden\n'


def rx_function():
	global ser, stop
	while stop!=1:
		while ser.inWaiting() > 0:
			output = ser.read(1)
			print output
			

def tx_function():
	global ser, stop, Wert0
#	while stop!=1:
	print ''
	Content = str(unichr(Wert0)) + str(unichr(Wert1)) + str(unichr(Wert2)) + str(unichr(Wert3)) + str(unichr(Wert4)) + str(unichr(Wert5)) + str(unichr(Wert6)) + str(unichr(Wert7)) + str(unichr(Wert8)) + str(unichr(Wert9))
#		time.sleep(0.5)
	ser.write(PreAmbel)
	ser.write(Content)

def tx_function2():
	global ser, stop
#	while stop!=1:
	print ''
	Content = str(unichr(Wert0)) + str(unichr(Wert1)) + str(unichr(Wert2)) + str(unichr(Wert3)) + str(unichr(Wert4)) + str(unichr(Wert5)) + str(unichr(Wert6)) + str(unichr(Wert7))
#		time.sleep(0.5)
	ser.write(PreAmbel)
	ser.write(Content)


def systick_function():
	global stop, TickCounter
	while stop!=1:
		TickCounter+=1
		time.sleep(0.1)

				



rx=threading.Thread(target=rx_function)
tx=threading.Thread(target=tx_function)
systick=threading.Thread(target=systick_function)

rx.start()
#tx.start()
#systick.start()

print 'Kann los gehen...\n\n'

while eingabe!="x":
	eingabe=raw_input('')

	if(eingabe == 'w'):
		mode = 'w'

	if(eingabe == 'r'):
		mode = 'r'

	if(eingabe == 'g'):
		mode = 'g'

	if(eingabe == 'b'):
		mode = 'b'

	if eingabe != 'x' and eingabe != 'w' and eingabe != 'b' and eingabe != 'g' and eingabe != 'r' :

		if mode == 'w':
			Wert0 = int(eingabe)
			if Wert0 > 24:
				Waert0 = 24
			print "Weiss: ", Wert0
			tx_function()

		if mode == 'r':
			Wert1 = int(eingabe)
			if Wert1 > 24:
				Waert1 = 24
			print "Rot: ", Wert1
			tx_function()

		if mode == 'g':
			Wert2 = int(eingabe)
			if Wert2 > 24:
				Waert2 = 24
			print "Gruen: ", Wert2
			tx_function()

		if mode == 'b':
			Wert3 = int(eingabe)
			if Wert3 > 24:
				Waert3 = 24
			print "Blau: ", Wert3
			tx_function()



stop=1
print 'stoped'
time.sleep(1)
ser.close()




