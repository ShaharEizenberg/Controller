import wx
import wx.lib.agw.aquabutton as AB
import wx.lib.agw.gradientbutton as GB
from pubsub import pub

class MyFrame(wx.Frame):
    def __init__(self, parent=None):
        super(MyFrame, self).__init__(parent, title="login", size=(500,500))
        self.initUI()
    def initUI(self):
        # create status bar
        self.statusbar = self.CreateStatusBar(1)

        # create main panel - to put on the other panels
        main_panel = MainPanel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(main_panel, 1, wx.EXPAND)

        self.SetSizer(box)
        self.Layout()
        self.Show()

class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.frame = parent
        self.SetBackgroundColour(wx.LIGHT_GREY)
        v_box = wx.BoxSizer()
        # create object for each panel
        self.login = StudentLoginPanel(self, self.frame)
        self.ui = StudentUI(self, self.frame)
        # add the panels
        v_box.Add(self.login)
        v_box.Add(self.ui)

        # show the first panel
        self.login.Show()
        self.SetSizer(v_box)
        self.Layout()






class StudentLoginPanel(wx.Panel):
    def __init__(self, parent, frame):
        wx.Panel.__init__(self, parent, pos=wx.DefaultPosition, size= (500, 500), style= wx.SIMPLE_BORDER)

        #pub.subscribe(self.my_listener, "panel_listener")

        self.frame = frame
        self.parent = parent
        self.SetBackgroundColour(wx.ColourDatabase().Find("DIM GREY"))
        #self.Hide()
        v_box = wx.BoxSizer(wx.VERTICAL)

        # title
        title = wx.StaticText(self,-1, label="Login Panel")
        titlefont = wx.Font(22, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        title.SetForegroundColour(wx.WHITE)
        title.SetFont(titlefont)

        # id
        idBox = wx.BoxSizer(wx.HORIZONTAL)
        idText = wx.StaticText(self, 1, label="ID: ")
        self.nameField = wx.TextCtrl(self, -1, name="ID", size = (150, -1))
        idText.SetForegroundColour(wx.WHITE)
        idFont = wx.Font(12, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        idText.SetFont(idFont)
        idBox.Add(idText, 0, wx.ALL, 5)
        idBox.Add(self.nameField, 0, wx.ALL, 5)


        #btnBox = wx.BoxSizer(wx.HORIZONTAL)
        #loginBtn = GB.GradientButton(self, label="login", size = (100, 40))
        #loginBtn.Bind(wx.EVT_BUTTON, self.onPressMe)

        loginBtn = AB.AquaButton(self, label="login", size = (100, 40))
        loginBtn.SetForegroundColour(wx.BLACK)
        loginBtn.SetBackgroundColour(wx.ColourDatabase().Find("VIOLET RED"))
        loginBtn.SetShadowColor(wx.ColourDatabase().Find("BLACK"))
        loginBtn.SetPulseOnFocus(True)
        loginBtn.Bind(wx.EVT_BUTTON, self.handle_login)

        v_box.AddSpacer(10)
        v_box.AddSpacer(10)
        v_box.AddSpacer(10)
        v_box.AddSpacer(10)
        v_box.Add(title, 0, wx.CENTER | wx.TOP, 5)
        v_box.AddSpacer(10)
        v_box.Add(idBox, 0, wx.CENTER | wx.ALL, 5)
        v_box.AddSpacer(10)
        v_box.Add(loginBtn, 0, wx.CENTER | wx.ALL, 5)

        # show the panel
        self.SetSizer(v_box)
        self.Layout()
        self.Hide()
            
    def handle_login(self, event):
        
        id = self.nameField.GetValue()
        if id == "":
            self.frame.SetStatusText("Must enter name an ID")
        elif len(id) < 9 or len(id) > 9:
            self.frame.SetStatusText("ID must be 9 digits")
        elif not id.isalnum():
            self.frame.SetStatusText("ID must be digits")
        else:
            #wx.CallAfter(pub.sendMessage, "login", message=id)
            pub.sendMessage("login", message= id)
            print("send id")
            self.Hide()
            self.parent.ui.Show()
            self.parent.Layout()

    def on_send_and_slose(self, event):
        """
        Send a message and close frame
        """
        msg = self.msg_txt.GetValue()
        # wx.CallAfter(pub.sendMessage, "panel_listener", message=msg)
        #pub.sendMessage("panel_listener", message=msg)
        #pub.sendMessage("panel_listener", message="test2", arg2= " 2nd argument!")
        self.Close()


class StudentUI(wx.Panel):
    """

    """
    def __init__(self, parent, frame):
        wx.Panel.__init__(self, parent, pos=wx.DefaultPosition, size= (500, 500), style= wx.SIMPLE_BORDER)
        self.frame = frame
        self.parent = parent
        self.SetBackgroundColour(wx.LIGHT_GREY)
        #self.SetBackgroundColour(wx.BLUE)
        v_box = wx.BoxSizer(wx.VERTICAL)

        # title
        title = wx.StaticText(self,-1, label="Hello -------")
        titlefont = wx.Font(22, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        title.SetForegroundColour(wx.BLACK)
        title.SetFont(titlefont)


        # the chat button
        bmp = wx.Bitmap("chat.png", wx.BITMAP_TYPE_ANY)
        chatButton = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp, size=(bmp.GetWidth() + 10, bmp.GetHeight() + 10))
        chatButton.Bind(wx.EVT_BUTTON, self.open_chat)

        # the help button
        helpBtn = AB.AquaButton(self, label="help", size=(100, 40))
        helpBtn.SetForegroundColour(wx.BLACK)
        helpBtn.SetBackgroundColour(wx.ColourDatabase().Find("VIOLET RED"))
        helpBtn.SetShadowColor(wx.ColourDatabase().Find("BLACK"))
        helpBtn.SetPulseOnFocus(True)
        helpBtn.Bind(wx.EVT_BUTTON, self.handle_help)



        v_box.Add(title, 0, wx.CENTER | wx.TOP, 5)
        v_box.AddSpacer(10)
        v_box.AddSpacer(10)
        v_box.Add(chatButton, 0, wx.CENTER | wx.ALL, 5)
        #v_box.AddSpacer(10)
        v_box.Add(helpBtn, 0, wx.CENTER | wx.ALL, 5)

        # show the panel
        #self.Show()
        self.SetSizer(v_box)
        self.Layout()

    def open_chat(self, event):
        """

        :param event:
        :return:
        """
        pass

    def handle_help(self, event):
        """

        :param event:
        :return:
        """
        self.frame.SetStatusText("your request was sent, waiting for the manager....")


ex = wx.App()
MyFrame(None)
ex.MainLoop()