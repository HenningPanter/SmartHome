import socket, threading, time

eingabe = ""

def Thread1():
  global eingabe
  UDP_IP = "192.168.0.111"
  UDP_PORT = 5555
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  while eingabe != "x":
    if eingabe != '':
      sock.sendto(eingabe, (UDP_IP, UDP_PORT))
      eingabe = ''
    time.sleep(0.5)
    

th1=threading.Thread(target=Thread1)
th1.start()

while eingabe !="x":
  eingabe = raw_input('')

time.sleep(1)
