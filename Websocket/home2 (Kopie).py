import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import time
import os
import threading
import Queue
import socket

text = ''

Wert0 = 1 # Befehl (0 -> lesen,  1-> schreiben)
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

weiss = 0
rot = 0
gruen = 0
blau = 0


def Thread1():
  global text
  print '\nStarte Thread.\n'
  UDP_IP = "192.168.0.45"
  UDP_PORT = 5555
  DEST_IP = "192.168.0.43"
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.bind((UDP_IP, UDP_PORT))

  DEST_IP_SONOFF_A = "192.168.0.111"
  DEST_IP_SONOFF_B = "192.168.0.112"
  DEST_IP_SONOFF_C = "192.168.0.113"
  DEST_IP_SONOFF_D = "192.168.0.114"
  DEST_IP_SONOFF_E = "192.168.0.115"
  DEST_IP_SONOFF_F = "192.168.0.116"


  sock_SONOFF = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


  while True:
    time.sleep(0.1)
    if text != '':
      print text

      if text == 'SONOFF_A_ON' or text == 'SONOFF_A_OFF':   # Modul A
        if text == 'SONOFF_A_ON':
          sock_SONOFF.sendto('an', (DEST_IP_SONOFF_A, UDP_PORT))
        if text == 'SONOFF_A_OFF':
          sock_SONOFF.sendto('aus', (DEST_IP_SONOFF_A, UDP_PORT))

      elif text == 'SONOFF_B_ON' or text == 'SONOFF_B_OFF':   # Modul B
        if text == 'SONOFF_B_ON':
          sock_SONOFF.sendto('an', (DEST_IP_SONOFF_B, UDP_PORT))
        if text == 'SONOFF_B_OFF':
          sock_SONOFF.sendto('aus', (DEST_IP_SONOFF_B, UDP_PORT))

      elif text == 'SONOFF_C_ON' or text == 'SONOFF_C_OFF':   # Modul C
        if text == 'SONOFF_C_ON':
          sock_SONOFF.sendto('an', (DEST_IP_SONOFF_C, UDP_PORT))
        if text == 'SONOFF_C_OFF':
          sock_SONOFF.sendto('aus', (DEST_IP_SONOFF_C, UDP_PORT))

      elif text == 'SONOFF_D_ON' or text == 'SONOFF_D_OFF':   # Modul D
        if text == 'SONOFF_D_ON':
          sock_SONOFF.sendto('an', (DEST_IP_SONOFF_D, UDP_PORT))
        if text == 'SONOFF_D_OFF':
          sock_SONOFF.sendto('aus', (DEST_IP_SONOFF_D, UDP_PORT))

      elif text == 'SONOFF_E_ON' or text == 'SONOFF_E_OFF':   # Modul E
        if text == 'SONOFF_E_ON':
          sock_SONOFF.sendto('an', (DEST_IP_SONOFF_E, UDP_PORT))
        if text == 'SONOFF_E_OFF':
          sock_SONOFF.sendto('aus', (DEST_IP_SONOFF_E, UDP_PORT))

      elif text == 'SONOFF_F_ON' or text == 'SONOFF_F_OFF':   # Modul F
        if text == 'SONOFF_F_ON':
          sock_SONOFF.sendto('an', (DEST_IP_SONOFF_F, UDP_PORT))
        if text == 'SONOFF_F_OFF':
          sock_SONOFF.sendto('aus', (DEST_IP_SONOFF_F, UDP_PORT))
      else:
        sock.sendto(text, (DEST_IP, UDP_PORT))    # wird an die Lichtdimmung auf Schrank geschickt

      text = ''

def Thread_Trockner_wieder_An():
  print 'Trockner aus\n'
  time.sleep(5)
  os.system("/usr/local/bin/gpio -g write 15 1")
  time.sleep(0.1)
  os.system("/usr/local/bin/gpio -g write 15 0")
  time.sleep(0.5)

  os.system("/usr/local/bin/gpio -g write 15 1")
  time.sleep(0.1)
  os.system("/usr/local/bin/gpio -g write 15 0")
  time.sleep(0.5)

  os.system("/usr/local/bin/gpio -g write 15 1")
  time.sleep(0.1)
  os.system("/usr/local/bin/gpio -g write 15 0")
  time.sleep(0.1)
  print 'Trockner an\n'


th1 = threading.Thread(target = Thread1)


class MainHandler(tornado.web.RequestHandler):
  def get(self):
    loader = tornado.template.Loader(".")
    self.write(loader.load("/media/usb/kram/WebSockets/home2.html").generate())

class WSHandler(tornado.websocket.WebSocketHandler):





  def open(self):
    global weiss, rot, gruen, blau
    Logfile = open('/media/usb/kram/WebSockets/home2.txt', 'a')
    log = time.asctime( time.localtime(time.time()) )
    log += ' : connection opened...\n'
    Logfile.write(log)
    print log
    Logfile.close()
    text = 'values:' + str(weiss) + '#' + str(rot) + '#' + str(gruen) + '#' + str(blau)
    self.write_message(text)
    text = ''

  def on_message(self, message):
    global text, Wert0, Wert1, Wert2, Wert3, Wert4, Wert5, Wert6, Wert7, Wert8, Wert9, Wert10, weiss, rot, gruen, blau

    DEST_IP_Werkstatt = "192.168.0.100"
    sock_Werkstatt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    if message == 'SONOFF_A_ON':
      text = 'SONOFF_A_ON'

    if message == 'SONOFF_A_OFF':
      text = 'SONOFF_A_OFF'



    if message == 'SONOFF_B_ON':
      text = 'SONOFF_B_ON'

    if message == 'SONOFF_B_OFF':
      text = 'SONOFF_B_OFF'




    if message == 'SONOFF_C_ON':
      text = 'SONOFF_C_ON'

    if message == 'SONOFF_C_OFF':
      text = 'SONOFF_C_OFF'




    if message == 'SONOFF_D_ON':
      text = 'SONOFF_D_ON'

    if message == 'SONOFF_D_OFF':
      text = 'SONOFF_D_OFF'




    if message == 'SONOFF_E_ON':
      text = 'SONOFF_E_ON'

    if message == 'SONOFF_E_OFF':
      text = 'SONOFF_E_OFF'




    if message == 'SONOFF_F_ON':
      text = 'SONOFF_F_ON'

    if message == 'SONOFF_F_OFF':
      text = 'SONOFF_F_OFF'





    if message.find("Weiss:") != -1:
      Wert1 = int(message[6:])
      weiss = Wert1
      text = str(unichr(Wert0)) + str(unichr(Wert1)) + str(unichr(Wert2)) + str(unichr(Wert3)) + str(unichr(Wert4)) + str(unichr(Wert5)) + str(unichr(Wert6)) + str(unichr(Wert7)) + str(unichr(Wert8)) + str(unichr(Wert9)) + str(unichr(Wert10))
      self.write_message(message)

    if message.find("Rot:") != -1:
      Wert2 = int(message[4:])
      rot = Wert2
      text = str(unichr(Wert0)) + str(unichr(Wert1)) + str(unichr(Wert2)) + str(unichr(Wert3)) + str(unichr(Wert4)) + str(unichr(Wert5)) + str(unichr(Wert6)) + str(unichr(Wert7)) + str(unichr(Wert8)) + str(unichr(Wert9)) + str(unichr(Wert10))
      self.write_message(message)

    if message.find("Gruen:") != -1:
      Wert3 = int(message[6:])
      gruen = Wert3
      text = str(unichr(Wert0)) + str(unichr(Wert1)) + str(unichr(Wert2)) + str(unichr(Wert3)) + str(unichr(Wert4)) + str(unichr(Wert5)) + str(unichr(Wert6)) + str(unichr(Wert7)) + str(unichr(Wert8)) + str(unichr(Wert9)) + str(unichr(Wert10))
      self.write_message(message)

    if message.find("Blau:") != -1:
      Wert4 = int(message[5:])
      blau = Wert4
      text = str(unichr(Wert0)) + str(unichr(Wert1)) + str(unichr(Wert2)) + str(unichr(Wert3)) + str(unichr(Wert4)) + str(unichr(Wert5)) + str(unichr(Wert6)) + str(unichr(Wert7)) + str(unichr(Wert8)) + str(unichr(Wert9)) + str(unichr(Wert10))
      self.write_message(message)

    if message == 'a1':
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 0 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 0 0")
      time.sleep(0.5)

      os.system("/usr/local/bin/gpio -g write 0 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 0 0")
      time.sleep(0.5)

      os.system("/usr/local/bin/gpio -g write 0 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 0 0")
      time.sleep(0.1)

#      self.write_message('AN!')

    if message == 'a2':
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 1 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 1 0")
      time.sleep(0.5)

      os.system("/usr/local/bin/gpio -g write 1 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 1 0")
      time.sleep(0.5)

      os.system("/usr/local/bin/gpio -g write 1 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 1 0")
      time.sleep(0.1)

#      self.write_message('AUS!')
#--------------------------------------------------

    if message == 'b1':
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 4 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 4 0")
      time.sleep(0.5)

      os.system("/usr/local/bin/gpio -g write 4 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 4 0")
      time.sleep(0.5)

      os.system("/usr/local/bin/gpio -g write 4 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 4 0")
      time.sleep(0.1)
#      self.write_message('AN!')

    if message == 'b2':
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 14 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 14 0")
      time.sleep(0.5)

      os.system("/usr/local/bin/gpio -g write 14 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 14 0")
      time.sleep(0.5)

      os.system("/usr/local/bin/gpio -g write 14 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 14 0")
      time.sleep(0.1)

      
#      self.write_message('AUS!')
#--------------------------------------------------

    if message == 'c1':
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 15 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 15 0")
      time.sleep(0.5)

      os.system("/usr/local/bin/gpio -g write 15 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 15 0")
      time.sleep(0.5)

      os.system("/usr/local/bin/gpio -g write 15 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 15 0")
      time.sleep(0.1)
      
#      self.write_message('AN!')

    if message == 'c2':
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 17 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 17 0")
      time.sleep(0.5)

      os.system("/usr/local/bin/gpio -g write 17 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 17 0")
      time.sleep(0.5)

      os.system("/usr/local/bin/gpio -g write 17 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 17 0")
      time.sleep(0.1)
      th2 = threading.Thread(target = Thread_Trockner_wieder_An)
      th2.start()
#      self.write_message('AUS!')
#--------------------------------------------------

    if message == 'd1':
      sock_Werkstatt.sendto('a_an', (DEST_IP_Werkstatt, 5555))
#      time.sleep(0.1)
#      os.system("/usr/local/bin/gpio -g write 18 1")
#      time.sleep(0.1)
#      os.system("/usr/local/bin/gpio -g write 18 0")

#      time.sleep(0.5)
#      os.system("/usr/local/bin/gpio -g write 18 1")
#      time.sleep(0.1)
#      os.system("/usr/local/bin/gpio -g write 18 0")

#      time.sleep(0.5)
#      os.system("/usr/local/bin/gpio -g write 18 1")
#      time.sleep(0.1)
#      os.system("/usr/local/bin/gpio -g write 18 0")
#      time.sleep(0.1)
#      self.write_message('AN!')

    if message == 'd2':
      sock_Werkstatt.sendto('a_aus', (DEST_IP_Werkstatt, 5555))
#      time.sleep(0.1)
#      os.system("/usr/local/bin/gpio -g write 21 1")
#      time.sleep(0.1)
#      os.system("/usr/local/bin/gpio -g write 21 0")

#      time.sleep(0.5)
#      os.system("/usr/local/bin/gpio -g write 21 1")
#      time.sleep(0.1)
#      os.system("/usr/local/bin/gpio -g write 21 0")

#      time.sleep(0.5)
#      os.system("/usr/local/bin/gpio -g write 21 1")
#      time.sleep(0.1)
#      os.system("/usr/local/bin/gpio -g write 21 0")
#      time.sleep(0.1)
#      self.write_message('AUS!')

      if message == 'read_all':
        text = 'values:' + str(weiss) + '#' + str(rot) + '#' + str(gruen) + '#' + str(blau)






#--------------------------------------------------

  def on_close(self):
    Logfile = open('/media/usb/kram/WebSockets/home2.txt', 'a')
    log = time.asctime( time.localtime(time.time()) )
    log += ' : connection closed...\n'
    Logfile.write(log)
    print log
    Logfile.close()





application = tornado.web.Application([
  (r'/ws', WSHandler),
  (r'/', MainHandler),
  (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./resources"}),
])

if __name__ == "__main__":
  th1.start()
  application.listen(9090)
  tornado.ioloop.IOLoop.instance().start()

