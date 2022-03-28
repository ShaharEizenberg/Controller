import queue
import threading
import socket
import select

def build_img(image, coordinates):
    """

    :param image: Image to send the client
    :param coordinates: Coordinates of the start difference box
    :return: Build message by protocol and return the message (The image and its parameters)
    """
    # Get the size of the image in bytes
    size = image.size
    # Compress the image to zip
    #send = zlib.compress(image.tobytes())
    send = image.tobytes()
    # The X, Y positions that the difference box starts
    x, y = str(coordinates[0]).zfill(4), str(coordinates[1]).zfill(4)
    param = ["01", str(size[0]).zfill(4),  str(size[1]).zfill(4), x, y, str(len(send)).zfill(20)]
    param = "#".join(param)
    param = str(len(param)) + param
    # Create the image massage
    send = param.encode() + send
    return send

def build_imgPrep(msg):
    """

    :param msg: the msg to send ("start share" or "stop share")
    :return: share preperation message (to end the share or to start it)
    """
    msg = "01" + "#" + msg
    return msg

def build_simpleMsg(msg):
    """

    :param msg: the message to send
    :return: build simple message by protocol (with message)
    """
    return

def build_shutInternet():
    """

    :return: a message to shut  the internet down (by protocol)
    """
    msg = "02" + "#" + "turnOfInternet"
    return msg

def build_login_ans(msg):
    """

    :return:
    """
    msg = "03" + "#" + msg
    return msg

def build_TurnOffComp():
    """

    :return: a message to turn of computer(by protocol)
    """
    msg = "04" + "#" + "turnOfComp"
    return msg

def build_chatMsg(msg, administrator):
    """

    :param administrator: the name of the administrator
    :param msg: the message to send
    :return: a chat message by protocol
    """
    msg = "05" + "#" + administrator + "#" + msg
    return msg

def build_lockCommand():
    """

    :return: build lock computer command by protocol
    """
    msg = "06" + "#" + "lock"
    return msg

def break_msg(msg):
    """

    :param msg: the message to break
    :return:
    """
    opcode = msg[:2]
    command = ""
    msg = msg.split("#")[1]
    if opcode == "02":
        command = "help"
    if opcode == "03":
        command = "chat"
    if opcode == "04":
        command = "exit"
    return command, msg



