import queue
import threading
import socket
import select
import Screen_shot
import time
import server_protocol


class Server:
    def __init__(self, port, recvQ):
        """

        :param port:
        :param servQ:
        """
        self.port = port
        print(self.port)
        self.recvQ = recvQ
        self.server_socket = None
        self.open_clients = {}
        self.running = False
        # the list of the clients to share the screen with
        self.share_list = []
        # start the threading (this thread receives messages from the server and insert them to the msg_q)
        threading.Thread(target=self._main_loop).start()

    def close_client(self, clientSocket):
        """

        :param clientSocket:
        :return:
        """
        del self.open_clients[clientSocket]
        try:
            clientSocket.close()
        except:
            pass

    def send(self, ip, msg):
        """
        the function sends a message to the server
        :param msg: message to the send to the server
        :return: None
        """
        print("in send")
        # create message
        msg = (str(len(msg)).zfill(2) + msg).encode()
        print(ip)
        client = self._find_socket_by_ip(ip)
        try:
            print("in send msg = ", msg)
            client.send(msg)
        except Exception as e:
            print("send in server", str(e))
            # if can't send the message, stop the thread
            self.close_client(client)
        """
        # send the message
        for client in self.open_clients.keys():
            if self.open_clients[client] == ip:
                try:
                    print("in send msg = ", msg)
                    client.send(msg)
                except Exception as e:
                    print("send in server", str(e))
                    # if can't send the message, stop the thread
                    self.close_client(client)
        """


    def _main_loop(self):
        """
        the function connects to the server and receives messages from it and inserts them to msg_q
        :return: None
        """
        print("in")
        self.server_socket = socket.socket()
        self.server_socket.bind(("0.0.0.0", self.port))
        self.server_socket.listen(4)
        self.running = True
        while self.running:
            rlist, wlist, xlist = select.select(list(self.open_clients.keys()) + [self.server_socket], list(self.open_clients.keys()), [], 0.3)
            for current_socket in rlist:
                if current_socket is self.server_socket:
                    # accept new client
                    client, address = self.server_socket.accept()
                    print(f'{address[0]} - connected')
                    self.open_clients[client] = address[0]
                else:
                    try:
                        # receive the length of the data
                        data_len = current_socket.recv(2).decode()
                        # receive the data from the server
                        data = current_socket.recv(int(data_len)).decode()
                    except:
                        # if can't receive from the client, close the socket with this client
                        self.close_client(current_socket)
                        print("out")
                    else:
                        # insert the message to the msg_q
                        self.recvQ.put([self.open_clients[current_socket], data])

    def _share_screen(self, client):
        """

        :param client: The client to share with him the screen
        :return: While the flag True - keep sharing the screen
        """
        print(client)
        self.share_list.append(client)
        # Takes the first screen shot
        img1 = Screen_shot.screenShot()
        # Build the image message by protocol
        send = server_protocol.build_img(img1, (0, 0))
        print("!!k ", send[:30].decode())
        try:
            # Send the first image to the client
            client.sendall(send)
            print("sent")
        except Exception as e:
            print(e)
        while self.recvQ.empty():
            pass
        msg = self.recvQ.get()
        while msg[0] != self.open_clients[client]:
            if not self.recvQ.empty():
                msg = self.recvQ().get()
        # keep sharing screen
        while client in self.share_list:
            print("k,jk,")
            # Take screen shot
            img2 = Screen_shot.screenShot()
            # Get the coordinates - the start, end of the difference box between image one to image two
            coordinates = Screen_shot.equal(img1, img2)

            # --- If there is difference between the images ---
            if coordinates != None:
                # Cut the difference box between image one to image two
                cut = img2.crop(coordinates)
                # Build the image message by protocol
                send = server_protocol.build_img(cut, coordinates[:2])
                try:
                    #print("try to send")
                    #print(len(send))
                    # Send image to the client
                    #print(type(client))
                    #client.send("03try".encode())
                    print("before sending")
                    client.sendall(send)
                    print("sent")
                except Exception as e:
                    print("faild sending the image")
                    print(e)

                # Paste image 2 on image 1
                Screen_shot.paste_on_img(img2, img1, (coordinates[0], coordinates[1]))
                #time.sleep(0.01)
                print("inn")
        print("out")

    def share_screen(self, client):
        """

        :return:
        """
        # start the threading (this thread receives messages from the server and insert them to the msg_q)
        threading.Thread(target=self._share_screen, args= (client,)).start()



    def _find_socket_by_ip(self, ip):
        """

        :param ip: the ip of the client
        :return: the sockets of the required client (regular socket and screen share socket)
        """
        client = None
        for socket in self.open_clients:
            if self.open_clients[socket] == ip:
                client = socket
                break
        return client

    def close_server(self):
        """

        :return:
        """
        clients = list(self.open_clients.keys())
        for client in clients:
            try:
                client.close()
            except:
                pass
        self.running = False
        self.open_clients.clear()
        self.server_socket.close()

#server = Server(2000, queue.Queue())