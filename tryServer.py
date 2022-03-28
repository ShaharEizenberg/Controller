import socket
from PIL import ImageGrab, Image
import zlib
import select
import threading
import time

def equal(image1, image2):
    """

    :param image1: The old image
    :param image2: The new image
    :return: Returns the bounding box of the difference between the two images
    """
    # Load the first image
    image1.load()
    # Load the second image
    image2.load()
    # The coordinates of the start and the end of the difference box
    coordinates = image1._new(image1.im.chop_difference(image2.im)).getbbox()
    # If the size is to close to the size of the screen send the whole screen
    if coordinates != None and coordinates[2] - coordinates[0] > 1200 and coordinates[3] - coordinates[1] > 700:
        coordinates = (0, 0, 1920, 1080)
    # Return the coordinates of the start and the end of the difference box
    return coordinates




def send_iamge(image, coordinates):
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


def share_screen(client):
    """

    :param client: The client to share with him the screen
    :return: While the flag True - keep sharing the screen
    """
    # Takes the first screen shot
    img1 = ImageGrab.grab()
    # Build the image message by protocol
    send = send_iamge(img1, (0, 0))
    try:
        # Send the first image to the client
        client.sendall(send)
    except Exception as e:
        print(e)
    # keep sharing screen
    while flag:
        # Take screen shot
        img2 = ImageGrab.grab()
        # Get the coordinates - the start, end of the difference box between image one to image two
        coordinates = equal(img1, img2)

        # --- If there is difference between the images ---
        if coordinates != None:
            # Cut the difference box between image one to image two
            cut = img2.crop(coordinates)
            # Build the image message by protocol
            send = send_iamge(cut, coordinates[:2])
            try:
                # Send image to the client
                client.sendall(send)
            except Exception as e:
                print(e)

            # Paste image 2 on image 1
            Image.Image.paste(img2, img1, (coordinates[0], coordinates[1]))
            time.sleep(0.01)


# socket : IP
open_clients = {}

# --- create server socket ---
server_soc = socket.socket()
server_soc.bind(("0.0.0.0", 1430))
server_soc.listen(4)

# While flag is True keep sharing the screen
global flag
flag = False

while True:
    rlist, wlist, xlist = select.select(list(open_clients.keys())+[server_soc],list(open_clients.keys()),[],0.3)
    for current_socket in rlist:
        # --- New client ---
        if current_socket is server_soc:
            # Get client socket, address - IP
            client, address = server_soc.accept()
            # Print that the client connected to the server
            print(f'{address[0]} - connected')
            # Add the client to the open sockets dictionary
            open_clients[client] = address[0]
            try:
                # Make sure that the client ready to screen sharing
                client.send((str(len("sending image")).zfill(2) + "sending image").encode())
                # The length of the ready to screen sharing answer
                data_len = int(client.recv(2).decode())
                # Check that the client connected to screen sharing
                flag = client.recv(data_len).decode() == "ok"
            except Exception as e:
                print(e)
            # If the client is ready to screen share start screen sharing
            if flag:
                threading.Thread(target=share_screen, args=(client,)).start()
