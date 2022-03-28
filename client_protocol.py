import queue
import socket
import threading

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
    x, y = str(coordinates[0]).zfill(4).encode(), str(coordinates[1]).zfill(4).encode()
    # Create the image massage
    send = (str(size[0]).zfill(4) + str(size[1]).zfill(4)).encode() + x + y + str(len(send)).zfill(20).encode() + send
    return send

def build_simpleMsg(msg):
    """

    :param msg: the message to send
    :return: build simple message by protocol (with message)
    """
    return

def build__helpMsg():
    """

    :return: a message to shut  the internet down (by protocol)
    """
    msg = "02" + "#" + "turnOfInternet"
    return msg


def build_chatMsg(msg):
    """

    :param msg: the message to send
    :return: a chat message by protocol
    """
    msg = "04" + "#" + msg
    return msg


def seperateImg(msg):
    """

    :param msg: the image parameters msg
    :return: the image parameters
    """
    print(msg)
    msg = msg.split("#")[1:]
    print(msg)
    # Receive the width of the image
    width_image = int(msg[0])
    # Receive the height of the image
    height_image = int(msg[1])
    # Receive the coordinates of the image
    coordinates = (int(msg[2]), int(msg[3]))
    # Receive the length (by bytes) of the image
    len_image = int(msg[4])
    return [width_image, height_image, coordinates, len_image]

def buildLoginMsg(id, macAdress):
    """

    :param id: the id of the student
    :param macAdress: the mac address of the students' computer
    :return: loginMsg
    """
    msg = "03" +"#"+ id + "#" + macAdress
    #msg = len(msg) + msg
    return msg

def build_command_succeeded(succeed, command):
    """

    :param command: the command to do
    :param succeed: True if the command had succeeded, else False
    :return: command succeeded message by protocol
    """
    msg = "00" + "#"
    if succeed:
        msg += command + "#" + "01"
    else:
        msg += command + "#" + "00"
    return msg


def break_msg(data):
    '''

    :param data:
    :return:
    '''
    opcode = data[0:2]
    status = data[3:]
    print("status: ", status)
    print(data)
    command = ""
    if opcode == "03":
        command = "login"
    print("command: ", command)
    return command, status

def build_exitMsg():
    """

    :return: an exit message
    """
    return "04" + "#" + "exit"

