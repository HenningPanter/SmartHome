import threading, queue

new_data_queue = queue.Queue()

running = True

modbus_server_ip = "192.168.0.144"

register_count = 15000

modbus_register = []
modbus_register_mutex = threading.Lock()

global_scan_tirgger = False

connected_clients = 0

soc = 101
p_pv = 0