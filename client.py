import queue
import socket
import threading
from setting import GENERAL_PORT, SCREEN_PORT
import pygame
import pyautogui
import client_protocol
import Screen_shot

class Client:
    def __init__(self, ip, port, clientQ):
        """

        :param ip:
        :param port:
        :param clientQ:
        """
        self.ip = ip
        self.port = port
        self.clientQ = clientQ
        self.my_socket = None
        self.running = False
        if port == GENERAL_PORT:
            self.shareClient = Client(ip, 3000, queue.Queue())
        self.screen = None
        # start the threading (this thread receives messages from the server and insert them to the msg_q)
        threading.Thread(target=self._main_loop).start()
        self.running = False

    def send(self, msg):
        """
        the function sends a message to the server
        :param msg: message to the send to the server
        :return: None
        """
        try:
            if type(msg) == str:
                # if the message is string, encode it
                msg = (str(len(msg)).zfill(2) + msg).encode()
            else:
                # if the message isn't string it means it's encrypted, so encode only the length of the message
                msg = str(len(msg)).zfill(2).encode() + msg
            # send the message
            self.my_socket.send(msg)
        except:
            # if can't send the message, stop the thread
            self.running = False

    def _main_loop(self):
        """
        the function connects to the server and receives messages from it and inserts them to msg_q
        :return: None
        """
        try:
            print("try in")
            self.my_socket = socket.socket()
            # connect to the server
            self.my_socket.connect((self.ip, self.port))
            print("succeded")
            #connect to the share screen server

            # if the connection succeeded, start threading
            self.running = True
        except:
            # if there was a problem to connect to the server, stop threading
            self.running = False
        # while there is a connection with the server:
        while self.running:
            data = ""
            try:
                # receive the length of the data
                data_len = int(self.my_socket.recv(2).decode())
                data = self.my_socket.recv(data_len).decode()
                print("received message")
                opcode = data[:2]
                print(opcode)
                print(data[3:])
                if opcode == '01' and self.port == SCREEN_PORT:
                    if data[3:] == "share screen":
                        print("open pygame")
                        self.open_pygame()
                    elif data[3:] == "stop share":
                        pygame.quit()
                    else:
                        print("receiving")
                        print(data_len)
                        # get image parameters
                        width, height, coordinate, length = client_protocol.seperateImg(data)
                        print(coordinate, width, height, length)
                        # receive the image by parameters
                        self.recv_img(coordinate, width, height, length)
                else:
                    # insert the message to the msg_q
                    self.clientQ.put(data)
                """
                elif opcode == '01':
                    if data[3:] == "share screen":
                        print("open pygame")
                        self.open_pygame()
                    elif data[3:] == "stop share":
                        pygame.quit()
                """
            except:
                # if can't receive from the server, stop threading
                self.running = False
            else:
                print(data)
                # insert the message to the msg_q
                self.clientQ.put(data)

    def open_pygame(self):
        """

        :return:
        """
        # Initialize pygame
        pygame.init()
        # The width, height of the full screen
        width, height = pyautogui.size()
        # Open pygame window in the size of the whole screen
        self.screen = pygame.display.set_mode((width, height))
        # Set caption of the screen
        pygame.display.set_caption('screen sharing')
        pygame.display.update()
        self.send("ok")

    def recv_img(self, coordinate, width, height, length):
        """

        :return:
        """
        file_data = bytearray()
        while len(file_data) < length:
            # put in size the amount of the bytes that has not copied from the image yet
            size = length - len(file_data)
            # try to receive 1024 bytes from the image each time
            try:
                if size > 2048:
                    # if there are 2048 bytes or more that has not copied from the image, copy 1024 bytes
                    file_data.extend(self.my_socket.recv(2048))
                else:
                    # if there are less than 1024 bytes that has not copied, copy the rest
                    file_data.extend(self.my_socket.recv(size))
            except Exception as e:
                print(str(e))
                # if there is a problem to receive the image, close the socket
                self.my_socket.close()
                file_data = None
                break
        print("succeeded receiving the image")
        Screen_shot.draw(file_data, coordinate, width, height, self.screen)


    def server_status(self):
        """

        :return: return the connection status (true - there is connection, false - there is no connection)
        """
        return self.running

    def close_client(self):
        """

        :return:
        """
        self.my_socket.close()
