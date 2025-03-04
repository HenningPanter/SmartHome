
#NOTE: You will have to update the ip address in index.html

import tornado.ioloop, tornado.web, tornado.websocket, tornado.template, json, glob_var, time
from logger import *

def unsigned_to_signed(n, bits=32):
    if n & (1 << (bits - 1)):
        return n - (1 << bits)
    else:
        return n


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        loader = tornado.template.Loader(".")
        self.write(loader.load("index.html").generate())
        

class WSHandler(tornado.websocket.WebSocketHandler):

    def __init__(self, base_value1, base_value2):
        super().__init__(base_value1, base_value2 )
        self.client_ip = self.request.remote_ip
        self.count = 0
        self.client_timeout = time.time()

    def format_power(self, number):
        if number > 999:
            return f" {(number/1000):.3f} kW"
        else:
            return str(number) + " Watt"



    def periodic_task(self):
        value = 999
        dictionary = {}
        p_pv = 0
        p_verbrauch = 0

        #######  SOC  ##########
        try:
            with glob_var.modbus_register_mutex:
                value = glob_var.modbus_register[13022] / 10
        except:
            pass

        dictionary["soc"] = f" {value:.1f}" + " %"


        #######  PV Leistung  ##########
        try:
            with glob_var.modbus_register_mutex:
                value = glob_var.modbus_register[5016]
                value += glob_var.modbus_register[5017] << 16
                p_pv = value
                value /= 1000
        except:
            pass

        dictionary["p_pv"] = f" {value:.3f}" + " kW" # (Register 5016)




        #######  PV1 Leistung  Spannung Strom ##########
        try:
            with glob_var.modbus_register_mutex:
                Spannung = glob_var.modbus_register[5010]
                Spannung /= 10
                Strom = glob_var.modbus_register[5011]
                Strom /= 10

                p1_pv = Spannung * Strom
                p1_pv /= 1000
        except:
            pass

        dictionary["p1_pv"] = f" {p1_pv:.3f}" + " kW"
        dictionary["u1_pv"] = f" {Spannung:.1f}" + " V"
        dictionary["i1_pv"] = f" {Strom:.1f}" + " A"




        #######  PV2 Leistung  Spannung Strom ##########
        try:
            with glob_var.modbus_register_mutex:
                Spannung = glob_var.modbus_register[5012]
                Spannung /= 10
                Strom = glob_var.modbus_register[5013]
                Strom /= 10

                p1_pv = Spannung * Strom
                p1_pv /= 1000
        except:
            pass

        dictionary["p2_pv"] = f" {p1_pv:.3f}" + " kW"
        dictionary["u2_pv"] = f" {Spannung:.1f}" + " V"
        dictionary["i2_pv"] = f" {Strom:.1f}" + " A"






        #######  Aktueller Verbrauch  ##########
        try:
            with glob_var.modbus_register_mutex:
                value = glob_var.modbus_register[13007]
                value += glob_var.modbus_register[13008] << 16
                p_verbrauch = value
                value /= 1000
        except:
            pass

        dictionary["verbrauch_aktuell"] = f" {value:.3f}" + " kW" # (Register 13007)
        # dictionary["verbrauch_aktuell"] = self.format_power(value) # (Register 13007)


        # #######  active power  ##########
        # try:
        #     with glob_var.modbus_register_mutex:
        #         value = glob_var.modbus_register[13033]
        #         value += glob_var.modbus_register[13034] << 16
        #         value /= 1000
        # except:
        #     pass
        # dictionary["active_power"] = f" {value:.3f}" + " kW" # (Register 13033)


        #######  Leistung Netz I/O  ##########
        try:
            with glob_var.modbus_register_mutex:
                value = glob_var.modbus_register[13009]
                value += glob_var.modbus_register[13010] << 16
                value = unsigned_to_signed(value)
                value /= 1000
        except:
            pass

        dictionary["ac_netz_io"] = f" {value:.3f}" + " kW" # (Register 13009)


        #######  Batterie Spannung  ##########
        try:
            with glob_var.modbus_register_mutex:
                value = glob_var.modbus_register[13019]
                # value = numpy.int32(value)
                value /= 10
        except:
            pass

        dictionary["batterie_spannung"] = f" {value:.1f}" + " V" # (Register 13019)

        #######  Batterie Strom  ##########
        try:
            with glob_var.modbus_register_mutex:
                value = glob_var.modbus_register[13020]
                value /= 10
                if p_pv < p_verbrauch:
                    value *= -1
        except:
            pass

        dictionary["batterie_strom"] = f" {value:.1f}" + " A" # (Register 13020)

        #######  Batterie Ladeleistung  ##########
        try:
            with glob_var.modbus_register_mutex:
                value = glob_var.modbus_register[13021]
                value /= 1000
                if p_pv < p_verbrauch:
                    value *= -1
        except:
            pass

        dictionary["batterie_power"] = f" {value:.3f}" + " kW" # (Register 13021)







        json_str = json.dumps(dictionary)
        try:
            self.write_message(json_str)
        except:
            self.close()


        ##################### client timeout monitor  #########################

        if time.time() - self.client_timeout > 10:
            self.close()






    def test_function(self, content):
        out_text = "{\"Nr\": " + str(5) + ", \"Name\": \"" + "Klaus" + "\"}"
        self.write_message(out_text)


    def open(self):
        glob_var.connected_clients += 1
        log_function(str(self.client_ip) + " opened website")
        log_function("connected clients: " + str(glob_var.connected_clients))
        # self.write_message("Hallo Welt")
        self.callback = tornado.ioloop.PeriodicCallback(self.periodic_task, 1000)
        self.callback.start()

    def on_message(self, message):
        self.client_timeout = time.time()

        if "global_scan" in message:
            glob_var.global_scan_tirgger = True


    def on_close(self):
        self.callback.stop()
        glob_var.connected_clients -= 1
        log_function(str(self.client_ip) + " closed website")
        log_function("connected clients: " + str(glob_var.connected_clients))

web_application = tornado.web.Application([(r'/ws', WSHandler), (r'/', MainHandler), (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./resources"}), ])


