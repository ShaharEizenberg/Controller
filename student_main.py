from client import Client
import queue
from pubsub import pub
from uuid import getnode
import client_protocol

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
    client1.send(msg)

pub.subscribe(handle_student_login, "login")

serverQ = queue.Queue()
clientQ = queue.Queue()


client1 = Client("192.168.1.30", 2000, clientQ)
while not client1.running:
    pass

#pub.sendMessage("panel_listener", message=msg)
pub.subscribe(handle_student_login, "login")
msg = ""  # input("enter msg or exit to quit ").lower()
while not msg == "exit":
    #print(f"client get back: {clientQ.get()}")
    #msg = input("Enter msg or exit to quit ").lower()
    pass

client1.close_client()
#main_server.close_server()
print("end programing")