def format_power(number):
    if number > 999:
        return f" {(number/1000):.3f} kw" 
    else:
        return str(number) + " Watt"


print(format_power(900))


# ##### unsigned to signed  ###############

# def unsigned_to_signed(n, bits=32):
#     if n & (1 << (bits - 1)):
#         return n - (1 << bits)
#     else:
#         return n

# value = 0xfffffffe

# signed_value = unsigned_to_signed(value)

# print(signed_value)











#############  formated numbers  ###############
# num = 2.4
# string = f" {num:.3f}"
# print(string)






#############   kill signal processing  ###################

# import signal, time

# running = True

# def handler_stop_signals(signum, frame):
#     global running
#     print("Killed by User")
#     running = False


# signal.signal(signal.SIGINT, handler_stop_signals)
# signal.signal(signal.SIGTERM, handler_stop_signals)


# while running:
#     time.sleep(1)

# print("quit")










##################  CSV to dict  ###################

# datei = open("ModbusRegister.csv", "r")
# content = datei.read()
# datei.close()

# content = content.splitlines()

# liste = []
# dic = {}
# for e in content:
#     worte = e.split(",")
#     dic['Register'] = int(worte[0])
#     dic['Name'] = worte[2]
#     dic['Einheit'] = worte[3]
#     try:
#         dic['Faktor'] = float(worte[4])
#     except:
#         dic['Faktor'] = 0
#     dic['word_count'] = int(worte[5])

#     liste.append(dic.copy())


# text = str(liste)

# datei = open("lookup_table.py", "w")
# datei.write(text)
# datei.close()

