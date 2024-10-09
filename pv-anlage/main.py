from pyModbusTCP.client import ModbusClient
import time, threading, glob_var, signal, os
from logger import *
from lookup_table import *
from website import *
from datetime import datetime

def handler_stop_signals(signum, frame):
    log_function("Killed by User")
    glob_var.running = False
    time.sleep(3)
    os.kill(os.getpid(), signal.SIGQUIT)


signal.signal(signal.SIGINT, handler_stop_signals)
signal.signal(signal.SIGTERM, handler_stop_signals)






class pv_monitor:

    def __init__(self):
        check_make_logfolder()
        log_function("program started")
        self.data_was_read_at_least_once = False

        self.u1_alt = 0
        self.i1_alt = 0
        self.u2_alt = 0
        self.i2_alt = 0
        self.register_init()
        self.read_thread = threading.Thread(target=self.read_thread_function).start()


    def register_init(self):
        for e in range(glob_var.register_count):
            glob_var.modbus_register.append(0)

    def insert_array(self, new_data, position, count):
        u1 = 0
        u2 = 0
        i1 = 0
        i2 = 0

        p = 0

        with glob_var.modbus_register_mutex:
            for e in range(count):
                if glob_var.modbus_register[position + e] != new_data[e]:
                    # entry = {(position + e): new_data[e]}
                    # if self.data_was_read_at_least_once:
                        # glob_var.new_data_queue.put(entry)
                    glob_var.modbus_register[position + e] = new_data[e]
            
            if position == 5010:
                u1 = glob_var.modbus_register[position] / 10
                i1 = glob_var.modbus_register[position + 1] / 10
                u2 = glob_var.modbus_register[position + 2] / 10
                i2 = glob_var.modbus_register[position + 3] / 10
                p = glob_var.modbus_register[position + 4]

                if self.u1_alt != u1 or self.i1_alt != i1 or self.u2_alt != u2 or self.i2_alt != i2:
                    self.u1_alt = u1
                    self.i1_alt = i1
                    self.u2_alt = u2
                    self.i2_alt = i2
                    # self.calculate_power(u1, u2, i1, i2, p)

                    log_value_function(f"u1: {u1:5.1f}   u2: {u2:5.1f}   i1: {i1:5.1f}   i2: {i2:5.1f}   p: {p}")



    def reinit_register(self):
        with glob_var.modbus_register_mutex:
            for e in range(glob_var.register_count):
                glob_var.modbus_register[e] = 999



    def log_thread_function(self):
        while True:
            if not glob_var.new_data_queue.empty():
                content = glob_var.new_data_queue.get()
                print("register " + str(list(content.keys())[0]) + " : " + str())################################################################# hier weitermachen
                try:
                    entry = glob_var.look_up_dict[content]
                    print(entry)
                    # log_function()
                except:
                    pass

            else:
                time.sleep(0.01)



    def read_thread_function(self):

        client = ModbusClient(glob_var.modbus_server_ip, port=502)

        connection_error_counter = 0

        p1 = 0
        p2 = 0

        p_gesamt = 0
        p_gesamt_alt = 0

        try:
            ret = client.open()
            log_function("modbus client: " + str(ret) + " opened")
        except:
            log_function("no connection to modbus server (at starting programm)")
            return

        

        while glob_var.running and connection_error_counter < 10:

            

            # content = client.read_input_registers(5000, 36)
            # self.insert_array(content, 5000, 36)
            # time.sleep(0.1)
            
            # content = client.read_input_registers(6226, 12)
            # self.insert_array(content, 6226, 12)
            # time.sleep(0.1)
                        
            #content = client.read_input_registers(6416, 12)
            #self.insert_array(content, 6416, 12)
            # time.sleep(0.1)
            
            content = client.read_input_registers(13007, 28)

            if content != None:
                self.insert_array(content, 13007, 28)
                connection_error_counter = 0
            else:
                self.reinit_register()
                log_function("Error reading modbus. Restarting connection...")
                try:
                    client.close()
                except:
                    pass
                
                time.sleep(10 * connection_error_counter)

                try:
                    ret = client.open()
                    log_function("modbus client: " + str(ret) + " opened")
                except:
                    connection_error_counter += 1
                    log_function("no connection to modbus server. Error-Counter: " + str(connection_error_counter))



            content = client.read_input_registers(5010, 11)
            
            if content != None:
                self.insert_array(content, 5010, 11)
                connection_error_counter = 0
            else:
                self.reinit_register()
                log_function("Error reading modbus. Restarting connection...")
                try:
                    client.close()
                except:
                    pass

                time.sleep(10 * connection_error_counter)

                try:
                    ret = client.open()
                    log_function("modbus client: " + str(ret) + " opened")
                except:
                    connection_error_counter += 1
                    log_function("no connection to modbus server. Error-Counter: " + str(connection_error_counter))





            # if abs(content[6] - p_gesamt) > 10:
            #     p1 = (content[0] / 10) * (content[1] / 10)
            #     p2 = (content[2] / 10) * (content[3] / 10)
            #     p_gesamt = content[6]

            #     aktueller_zeitstempel = datetime.now()
            #     formatierter_zeitstempel = aktueller_zeitstempel.strftime("%d.%m.%Y  %H:%M:%S Uhr:")
            #     print(str(formatierter_zeitstempel) + "    P-Sonne: " +  str(round((p_gesamt / 1000), 2)) + " kW")



            
            self.data_was_read_at_least_once = True



            # trigger global scan

            if glob_var.global_scan_tirgger == True:
                glob_var.global_scan_tirgger = False
                ret_val = client.write_multiple_registers(30230, [0xAA])
                log_function("global scan triggered. ret_val: " + str(ret_val))


            time.sleep(2)
        
        client.close()
        log_function("modbus client closed")







if __name__ == "__main__":

    monitor = pv_monitor()
    web_application.listen(3333)
    tornado.ioloop.IOLoop.instance().start()
