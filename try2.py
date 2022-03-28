from pubsub import pub
import threading
class Try:
    def __init__(self):
        pub.subscribe(self.check_it, 'panel_listener')
        # print(pub.isSubscribed(check_it, "panel_listener"))

    def check_it(self, msg):

        """

        :param msg:
        :return:
        """
        print("in")
        print(msg)


#pub.subscribe(check_it, "panel_listener")
#print(pub.isSubscribed(check_it, "panel_listener"))
try_it = Try()

while True:
    pass
