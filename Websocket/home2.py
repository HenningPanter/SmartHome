import tornado.ioloop, tornado.web, tornado.websocket, tornado.template
import time, threading, socket, datetime, json

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







sock_SONOFF = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

DEST_IP_SONOFF_A = "192.168.0.111"
DEST_IP_SONOFF_B = "192.168.0.112"
DEST_IP_SONOFF_C = "192.168.0.113"
DEST_IP_SONOFF_D = "192.168.0.114"
DEST_IP_SONOFF_E = "192.168.0.115"
DEST_IP_SONOFF_F = "192.168.0.116"

UDP_IP = "192.168.0.27"
UDP_PORT = 5555
DEST_IP = "192.168.0.43"


def UDP_Thread_function():
  global text
  
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.bind((UDP_IP, UDP_PORT))


  while True:
    time.sleep(0.005)
    if text != '':

      if text == 'SONOFF_A_ON' or text == 'SONOFF_A_OFF':   # Modul A
        if text == 'SONOFF_A_ON':
          sock_SONOFF.sendto(bytes('an', 'utf-8'), (DEST_IP_SONOFF_A, UDP_PORT))
        if text == 'SONOFF_A_OFF':
          sock_SONOFF.sendto(bytes('aus', 'utf-8'), (DEST_IP_SONOFF_A, UDP_PORT))

      elif text == 'SONOFF_B_ON' or text == 'SONOFF_B_OFF':   # Modul B
        if text == 'SONOFF_B_ON':
          sock_SONOFF.sendto(bytes('an', 'utf-8'), (DEST_IP_SONOFF_B, UDP_PORT))
        if text == 'SONOFF_B_OFF':
          sock_SONOFF.sendto(bytes('aus', 'utf-8'), (DEST_IP_SONOFF_B, UDP_PORT))

      elif text == 'SONOFF_C_ON' or text == 'SONOFF_C_OFF':   # Modul C
        if text == 'SONOFF_C_ON':
          sock_SONOFF.sendto(bytes('an', 'utf-8'), (DEST_IP_SONOFF_C, UDP_PORT))
        if text == 'SONOFF_C_OFF':
          sock_SONOFF.sendto(bytes('aus', 'utf-8'), (DEST_IP_SONOFF_C, UDP_PORT))

      elif text == 'SONOFF_D_ON' or text == 'SONOFF_D_OFF':   # Modul D
        if text == 'SONOFF_D_ON':
          sock_SONOFF.sendto(bytes('an', 'utf-8'), (DEST_IP_SONOFF_D, UDP_PORT))
        if text == 'SONOFF_D_OFF':
          sock_SONOFF.sendto(bytes('aus', 'utf-8'), (DEST_IP_SONOFF_D, UDP_PORT))

      elif text == 'SONOFF_E_ON' or text == 'SONOFF_E_OFF':   # Modul E
        if text == 'SONOFF_E_ON':
          sock_SONOFF.sendto(bytes('an', 'utf-8'), (DEST_IP_SONOFF_E, UDP_PORT))
        if text == 'SONOFF_E_OFF':
          sock_SONOFF.sendto(bytes('aus', 'utf-8'), (DEST_IP_SONOFF_E, UDP_PORT))

      elif text == 'SONOFF_F_ON' or text == 'SONOFF_F_OFF':   # Modul F
        if text == 'SONOFF_F_ON':
          sock_SONOFF.sendto(bytes('an', 'utf-8'), (DEST_IP_SONOFF_F, UDP_PORT))
        if text == 'SONOFF_F_OFF':
          sock_SONOFF.sendto(bytes('aus', 'utf-8'), (DEST_IP_SONOFF_F, UDP_PORT))
      else:
        sock.sendto(bytes(text, 'utf-8'), (DEST_IP, UDP_PORT))    # wird an die Lichtdimmung auf Schrank geschickt

      text = ''

def open_time_table_file():
    with open('timetable.json', 'r') as file:
        content = file.read()
    return json.loads(content)



def send_to_sonoff(command):

  if command == 'SONOFF_A_ON':
    sock_SONOFF.sendto(bytes('an', 'utf-8'), (DEST_IP_SONOFF_A, UDP_PORT))

  if command == 'SONOFF_A_OFF':
    sock_SONOFF.sendto(bytes('aus', 'utf-8'), (DEST_IP_SONOFF_A, UDP_PORT))

  if command == 'SONOFF_B_ON':
    sock_SONOFF.sendto(bytes('an', 'utf-8'), (DEST_IP_SONOFF_B, UDP_PORT))
  
  if command == 'SONOFF_B_OFF':
    sock_SONOFF.sendto(bytes('aus', 'utf-8'), (DEST_IP_SONOFF_B, UDP_PORT))
  
  if command == 'SONOFF_C_ON':
    sock_SONOFF.sendto(bytes('an', 'utf-8'), (DEST_IP_SONOFF_C, UDP_PORT))

  if command == 'SONOFF_C_OFF':
    sock_SONOFF.sendto(bytes('aus', 'utf-8'), (DEST_IP_SONOFF_C, UDP_PORT))

  if command == 'SONOFF_D_ON':
    sock_SONOFF.sendto(bytes('an', 'utf-8'), (DEST_IP_SONOFF_D, UDP_PORT))

  if command == 'SONOFF_D_OFF':
    sock_SONOFF.sendto(bytes('aus', 'utf-8'), (DEST_IP_SONOFF_D, UDP_PORT))

  if command == 'SONOFF_E_ON':
    sock_SONOFF.sendto(bytes('an', 'utf-8'), (DEST_IP_SONOFF_E, UDP_PORT))

  if command == 'SONOFF_E_OFF':
    sock_SONOFF.sendto(bytes('aus', 'utf-8'), (DEST_IP_SONOFF_E, UDP_PORT))

  if command == 'SONOFF_F_ON':
    sock_SONOFF.sendto(bytes('an', 'utf-8'), (DEST_IP_SONOFF_F, UDP_PORT))

  if command == 'SONOFF_F_OFF':
    sock_SONOFF.sendto(bytes('aus', 'utf-8'), (DEST_IP_SONOFF_F, UDP_PORT))



def Zeitsteuerung_Thread_function():
  schedule = open_time_table_file()

  while True:
    d = datetime.datetime.now()

    for e in schedule:
      if schedule[e]['Stunde'] == d.hour and schedule[e]['Minute'] == d.minute and schedule[e]['is_processed'] == False:
        schedule[e]['is_processed'] = True
        send_to_sonoff(schedule[e]['Aktion'])

      if schedule[e]['Stunde'] == d.hour and (schedule[e]['Minute'] + 1) == d.minute and schedule[e]['is_processed'] == True:
        schedule[e]['is_processed'] = False

    time.sleep(1)




th1 = threading.Thread(target = UDP_Thread_function)
th2 = threading.Thread(target = Zeitsteuerung_Thread_function)


class MainHandler(tornado.web.RequestHandler):
  def get(self):
    loader = tornado.template.Loader(".")
    self.write(loader.load("/home/henning/freigabe/smarthome/home2.html").generate())

class WSHandler(tornado.websocket.WebSocketHandler):

  def open(self):
    global weiss, rot, gruen, blau
    Logfile = open('/home/henning/freigabe/smarthome/home2.txt', 'a')
    log = time.asctime( time.localtime(time.time()) )
    log += ' : connection opened...\n'
    Logfile.write(log)
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
      text = str(chr(Wert0)) + str(chr(Wert1)) + str(chr(Wert2)) + str(chr(Wert3)) + str(chr(Wert4)) + str(chr(Wert5)) + str(chr(Wert6)) + str(chr(Wert7)) + str(chr(Wert8)) + str(chr(Wert9)) + str(chr(Wert10))
      self.write_message(message)

    if message.find("Rot:") != -1:
      Wert2 = int(message[4:])
      rot = Wert2
      text = str(chr(Wert0)) + str(chr(Wert1)) + str(chr(Wert2)) + str(chr(Wert3)) + str(chr(Wert4)) + str(chr(Wert5)) + str(chr(Wert6)) + str(chr(Wert7)) + str(chr(Wert8)) + str(chr(Wert9)) + str(chr(Wert10))
      self.write_message(message)

    if message.find("Gruen:") != -1:
      Wert3 = int(message[6:])
      gruen = Wert3
      text = str(chr(Wert0)) + str(chr(Wert1)) + str(chr(Wert2)) + str(chr(Wert3)) + str(chr(Wert4)) + str(chr(Wert5)) + str(chr(Wert6)) + str(chr(Wert7)) + str(chr(Wert8)) + str(chr(Wert9)) + str(chr(Wert10))
      self.write_message(message)

    if message.find("Blau:") != -1:
      Wert4 = int(message[5:])
      blau = Wert4
      text = str(chr(Wert0)) + str(chr(Wert1)) + str(chr(Wert2)) + str(chr(Wert3)) + str(chr(Wert4)) + str(chr(Wert5)) + str(chr(Wert6)) + str(chr(Wert7)) + str(chr(Wert8)) + str(chr(Wert9)) + str(chr(Wert10))
      self.write_message(message)

    if message == 'c2':
      sock_SONOFF.sendto(bytes('aus', 'utf-8'), (DEST_IP_SONOFF_C, UDP_PORT))




    if message == 'd1':
      sock_Werkstatt.sendto(bytes('a_an', 'utf-8'), (DEST_IP_Werkstatt, 5556))


    if message == 'd2':
      sock_Werkstatt.sendto(bytes('a_aus', 'utf-8'), (DEST_IP_Werkstatt, 5556))

    if message == 'pool_an':
      sock_Werkstatt.sendto(bytes('pool_an', 'utf-8'), (DEST_IP_Werkstatt, 5556))


    if message == 'pool_aus':
      sock_Werkstatt.sendto(bytes('pool_aus', 'utf-8'), (DEST_IP_Werkstatt, 5556))

    if message == 'read_all':
      text = 'values:' + str(weiss) + '#' + str(rot) + '#' + str(gruen) + '#' + str(blau)
    
    time.sleep(0.01)



#--------------------------------------------------

  def on_close(self):
    Logfile = open('/home/henning/freigabe/smarthome/home2.txt', 'a')
    log = time.asctime( time.localtime(time.time()) )
    log += ' : connection closed...\n'
    Logfile.write(log)
    Logfile.close()





application = tornado.web.Application([
  (r'/ws', WSHandler),
  (r'/', MainHandler),
  (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./resources"}),
])

if __name__ == "__main__":
  th1.start()
  th2.start()
  application.listen(9090)
  tornado.ioloop.IOLoop.instance().start()

