from client import Client
import queue
from pubsub import pub
from uuid import getnode
import client_protocol
import setting
from studentsUI import  *
import client_protocol
import threading

def get_macAddress():
    """ returns  mac address"""
    return ':'.join(['{:02x}'.format((getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])


def handle_student_login(id):
    """

    :param id: the id of the student
    :return:
    """
    print("check in function")
    msg = client_protocol.buildLoginMsg(id, get_macAddress())
    client.send(msg)







def handle_recv_q(rcv_q):
    print("in handle_recv_q")
    while True:
        data = rcv_q.get()
        command, status = client_protocol.break_msg(data)
        if command == "login":
            print("handle recv ", status)
            wx.CallAfter(pub.sendMessage, "login", status=status)






clientQ = queue.Queue()
client = Client(setting.SERVER_IP, setting.GENERAL_PORT, clientQ)


# while not client1.running:
#     pass

# #pub.sendMessage("panel_listener", message=msg)
# pub.subscribe(handle_student_login, "login")
# msg = ""  # input("enter msg or exit to quit ").lower()
# while not msg == "exit":
#     #print(f"client get back: {clientQ.get()}")
#     #msg = input("Enter msg or exit to quit ").lower()
#     pass
#
# client1.close_client()
#main_server.close_server()
# print("end programing")
threading.Thread(target= handle_recv_q, args= (clientQ,)).start()
ex = wx.App()
MyFrame(client,get_macAddress(), None)
ex.MainLoop()
client.send(client_protocol.build_exitMsg())