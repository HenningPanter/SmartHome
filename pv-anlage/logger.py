import datetime, os, threading

log_function_mutex = threading.Lock()

# erstellt logs folder wenn noch nicht existent
def check_make_logfolder():
    folder = './logs'
    if not os.path.exists(folder):
        os.makedirs(folder)


# schreibt content in log-file mit datum als Namen unter ./logs
def log_function(content):
    global log_function_mutex
    with log_function_mutex:
        current_date = datetime.datetime.now()
        data = current_date.isoformat().replace("T", "__") + " : " + content + "\n"
        filename = "./logs/" + str(current_date.date()) + ".log"
        f = open(filename, "a")
        f.write(data)
        f.close()

# schreibt content in log-file mit datum als Namen unter ./logs    fuer Betriebswerte
def log_value_function(content):
    global log_function_mutex
    with log_function_mutex:
        current_date = datetime.datetime.now()
        data = current_date.isoformat().replace("T", "__") + " : " + content + "\n"
        filename = "./logs/" + str(current_date.date()) + "_values.log"
        f = open(filename, "a")
        f.write(data)
        f.close()