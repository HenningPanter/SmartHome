import socket

Wert0 = 1 # Befehl (0-> lesen, 1->schreiben)
Wert1 = 0 # zu schreibende Werte 1 bis 10
Wert2 = 0
Wert3 = 0
Wert4 = 0
Wert5 = 0
Wert6 = 0
Wert7 = 0
Wert8 = 0
Wert9 = 0
Wert10 = 0

UDP_IP = "192.168.0.20"
UDP_PORT = 5555

DEST_IP = "192.168.0.43"
Frame = str(unichr(Wert0)) + str(unichr(Wert1)) + str(unichr(Wert2)) + str(unichr(Wert3)) + str(unichr(Wert4)) + str(unichr(Wert5)) + str(unichr(Wert6)) + str(unichr(Wert7)) + str(unichr(Wert8)) + str(unichr(Wert9)) + str(unichr(Wert10))
#Frame = "Hallo"
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

sock.sendto(Frame, (DEST_IP, UDP_PORT))
print 'Frame sent'

data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

if data == str(chr(1)):
	print 'length error'
else:
	print "received message:", data 
