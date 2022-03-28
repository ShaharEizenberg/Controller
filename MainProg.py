import server
import client
import queue
import time
import threading
import server_protocol
from pubsub import pub
import wx
from teacherUITT import *

# dictionary of mac address and students parameters
mac_parameters = {"64:00:6A:42:95:8E": ["0", "on", "on"]}
mac_name = {"64:00:6A:42:95:8E": "123456789"}
mac_ip = {"192.168.4.79": "64:00:6A:42:95:8E"}
# dictionary of mac address, student name
id_name = {"123456789": "Shahar Eizenberg"}

def handle_msg(recvQ):
    """
    the function handles the message from the client according to the opcode of the message
    :param msg: the msg from the client
    :return: None
    """
    while True:
        msg = recvQ.get()
        print("in handle_msg")
        print("in handle_msg")
        print(msg[1])
        ip, msg = msg[0], msg[1]
        msg = msg.split("#")
        print(msg)
        if msg[0] == "02":
            pass
        elif msg[0] == "03":
            macAddress, id = msg[2].upper(), msg[1]
            print(id)
            print(macAddress)
            print(type(macAddress))
            print(list(mac_name.keys()))
            #if
            if mac_name[macAddress] == id:
                status = id_name[id]
                position = int(mac_parameters[macAddress][0])
                wx.CallAfter(pub.sendMessage, "studentLogin", pos=position)
                #wx.CallAfter("studentLogin", pos=position)
            else:
                status = "fail"
            main_server.send(ip, server_protocol.build_login_ans(status))
        elif msg[0] == "04":
            position = int(mac_parameters[mac_ip[ip]][0])
            wx.CallAfter(pub.sendMessage, "student exit", pos=position)


serverQ1 = queue.Queue()
serverQ2 = queue.Queue()
#clientQ = queue.Queue()

main_server = server.Server(2000, serverQ1)

share_server = server.Server(3000, serverQ2)

msg = ""  # input("enter msg or exit to quit ").lower()
time.sleep(1)
clients = share_server.open_clients.keys()
print(clients)

threading.Thread(target=handle_msg, args= (serverQ1,)).start()
"""
while not msg == "exit":
    if not main_server.recvQ.empty():
        handle_msg(main_server.recvQ.get())
    #msg = input("Enter 1 to start share, 2 to start second share, 3 to stop first share or 4 to stop second share")
    if msg == "1":
        share_server.send("192.168.4.79", server_protocol.build_imgPrep("share screen"))
        print(list(share_server.open_clients.keys())[0])
        #threading.Thread(target=share_server.share_screen, args= (list(share_server.open_clients.keys())[0],))
        share_server.share_screen(list(share_server.open_clients.keys())[0])
    if msg == "2":
        main_server.send(share_server.open_clients[clients[1]], server_protocol.build_imgPrep("share screen"))
        share_server.share_screen(clients[1])
    if msg == "3":
        main_server.send(share_server.open_clients[clients[0]], server_protocol.build_imgPrep("stop share"))
        share_server.share_list.remove(clients[0])
    if msg == "4":
        main_server.send(share_server.open_clients[clients[1]], server_protocol.build_imgPrep("stop share"))
        share_server.share_list.remove(clients[1])
    if not main_server.recvQ.empty():
        msg = main_server.recvQ.get()
        handle_msg(msg)
"""

#client1.close_client()
#main_server.close_server()
#print("end programing")

ex = wx.App()
MyFrame(None)
ex.MainLoop()
