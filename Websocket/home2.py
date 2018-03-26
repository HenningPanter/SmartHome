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



def Thread1():
  global text
  print '\nStarte Thread.\n'
  UDP_IP = "192.168.0.45"
  UDP_PORT = 5555
  DEST_IP = "192.168.0.43"
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.bind((UDP_IP, UDP_PORT))
  while True:
    time.sleep(0.1)
    if text != '':
      print text
      sock.sendto(text, (DEST_IP, UDP_PORT))
      text = ''


th1 = threading.Thread(target = Thread1)

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    loader = tornado.template.Loader(".")
    self.write(loader.load("/media/usb/kram/WebSockets/home2.html").generate())

class WSHandler(tornado.websocket.WebSocketHandler):

  def open(self):
    Logfile = open('/media/usb/kram/WebSockets/home2.txt', 'a')
    log = time.asctime( time.localtime(time.time()) )
    log += ' : connection opened...\n'
    Logfile.write(log)
    print log
    Logfile.close()
    self.write_message("-")

  def on_message(self, message):
    global text, Wert0, Wert1, Wert2, Wert3, Wert4, Wert5, Wert6, Wert7, Wert8, Wert9, Wert10

    if message.find("Weiss:") != -1:
      Wert1 = int(message[6:])
      text = str(unichr(Wert0)) + str(unichr(Wert1)) + str(unichr(Wert2)) + str(unichr(Wert3)) + str(unichr(Wert4)) + str(unichr(Wert5)) + str(unichr(Wert6)) + str(unichr(Wert7)) + str(unichr(Wert8)) + str(unichr(Wert9)) + str(unichr(Wert10))
      self.write_message(message)

    if message.find("Rot:") != -1:
      Wert2 = int(message[4:])
      text = str(unichr(Wert0)) + str(unichr(Wert1)) + str(unichr(Wert2)) + str(unichr(Wert3)) + str(unichr(Wert4)) + str(unichr(Wert5)) + str(unichr(Wert6)) + str(unichr(Wert7)) + str(unichr(Wert8)) + str(unichr(Wert9)) + str(unichr(Wert10))
      self.write_message(message)

    if message.find("Gruen:") != -1:
      Wert3 = int(message[6:])
      text = str(unichr(Wert0)) + str(unichr(Wert1)) + str(unichr(Wert2)) + str(unichr(Wert3)) + str(unichr(Wert4)) + str(unichr(Wert5)) + str(unichr(Wert6)) + str(unichr(Wert7)) + str(unichr(Wert8)) + str(unichr(Wert9)) + str(unichr(Wert10))
      self.write_message(message)

    if message.find("Blau:") != -1:
      Wert4 = int(message[5:])
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
#      self.write_message('AUS!')
#--------------------------------------------------

    if message == 'd1':
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 18 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 18 0")

      time.sleep(0.5)
      os.system("/usr/local/bin/gpio -g write 18 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 18 0")

      time.sleep(0.5)
      os.system("/usr/local/bin/gpio -g write 18 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 18 0")
      time.sleep(0.1)
#      self.write_message('AN!')

    if message == 'd2':
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 21 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 21 0")

      time.sleep(0.5)
      os.system("/usr/local/bin/gpio -g write 21 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 21 0")

      time.sleep(0.5)
      os.system("/usr/local/bin/gpio -g write 21 1")
      time.sleep(0.1)
      os.system("/usr/local/bin/gpio -g write 21 0")
      time.sleep(0.1)
#      self.write_message('AUS!')
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

