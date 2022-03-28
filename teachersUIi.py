import wx
import wx.lib.agw.aquabutton as AB

class MyFrame(wx.Frame):
    def __init__(self, parent=None):
        super(MyFrame, self).__init__(parent, title="login", size=(1920,1080))
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
        self.login = LoginPanel(self, self.frame)
        self.ui = TeacherUI(self, self.frame)
        # add the panels
        v_box.Add(self.login)
        v_box.Add(self.ui)

        # show the first panel
        self.login.Show()
        self.SetSizer(v_box)
        self.Layout()



class LoginPanel(wx.Panel):
    def __init__(self, parent, frame):
        wx.Panel.__init__(self, parent, pos=wx.DefaultPosition, size=(1920, 1080), style=wx.SIMPLE_BORDER)
        self.frame = frame
        self.parent = parent
        self.font = wx.Font(20, wx.FONTFAMILY_ROMAN, wx.NORMAL, wx.NORMAL)
        self.SetBackgroundColour(wx.ColourDatabase().Find("DIM GREY"))
        v_box = wx.BoxSizer(wx.VERTICAL)

        # title
        title = wx.StaticText(self,-1, label="Login Panel")
        titlefont = wx.Font(80, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        title.SetForegroundColour(wx.WHITE)
        title.SetFont(titlefont)

        # username
        nameBox = wx.BoxSizer(wx.HORIZONTAL)
        nameText = wx.StaticText(self, 1, label="UserName: ")
        nameText.SetForegroundColour(wx.WHITE)
        self.nameField = wx.TextCtrl(self, -1, name="username", size = (310, 20))
        self.nameField.SetFont(self.font)
        self.nameField.SetMaxLength(20)
        #self.nameField.
        nameText.SetFont(self.font)
        nameBox.Add(nameText, 0, wx.ALL, 5)
        nameBox.Add(self.nameField, 0, wx.EXPAND | wx.ALL, 5)

        # password
        passBox = wx.BoxSizer(wx.HORIZONTAL)
        passText = wx.StaticText(self, 1, label="Password: ")
        passText.SetForegroundColour(wx.WHITE)
        self.passField = wx.TextCtrl(self, -1, name="username", size=(310, 20), style= wx.TE_PASSWORD)
        self.passField.SetFont(self.font)
        self.passField.SetMaxLength(17)
        passText.SetFont(self.font)
        passBox.Add(passText, 0, wx.ALL, 5)
        passBox.Add(self.passField, 0, wx.EXPAND | wx.ALL, 5)

        # the login button
        loginBtn = AB.AquaButton(self, label="login", size=(160, 60))
        loginBtn.SetForegroundColour(wx.BLACK)
        loginBtn.SetBackgroundColour(wx.ColourDatabase().Find("VIOLET RED"))
        loginBtn.SetShadowColor(wx.ColourDatabase().Find("BLACK"))
        loginBtn.SetPulseOnFocus(True)
        loginBtn.Bind(wx.EVT_BUTTON, self.handle_login)

        # add all the sizers to the main sizer
        for i in range(8):
            v_box.AddSpacer(10)
        v_box.Add(title, 0, wx.CENTER | wx.ALL, 5)
        v_box.AddSpacer(10)
        v_box.Add(nameBox, 0, wx.CENTER | wx.ALL, 5)
        v_box.Add(passBox, 0, wx.CENTER | wx.ALL, 5)
        v_box.AddSpacer(10)
        v_box.Add(loginBtn, 0, wx.CENTER | wx.ALL, 5)

        # show the panel
        self.SetSizer(v_box)
        self.Layout()

    def handle_login(self, event):
        """

        :return:
        """
        username = self.nameField.GetValue()
        password = self.passField.GetValue()
        if username == "" or password == "":
            self.frame.SetStatusText("Must enter name and password")
        else:
            self.frame.SetStatusText("waiting for Server approve")
            #--------------- wait for connection with the server ----------------------
            self.Hide()
            self.parent.ui.Show()
            self.parent.Layout()

class TeacherUI(wx.Panel):
    """

    """

    def __init__(self, parent, frame):
        wx.Panel.__init__(self, parent, pos=wx.DefaultPosition, size=(1920, 1080), style=wx.SIMPLE_BORDER)
        self.frame = frame
        self.parent = parent
        self.SetBackgroundColour(wx.Colour(78, 78, 82))
        # self.SetBackgroundColour(wx.BLUE)
        v_box = wx.BoxSizer(wx.VERTICAL)

        # title
        title = wx.StaticText(self, -1, label="Hello -------")
        titlefont = wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        title.SetForegroundColour(wx.BLACK)
        title.SetFont(titlefont)

        bmp = wx.Bitmap("no-internet.png", wx.BITMAP_TYPE_ANY)
        internetBtn = AB.AquaButton(self, bitmap=bmp, label="Turn of internet")
        internetBtn.SetForegroundColour(wx.BLACK)
        internetBtn.SetBackgroundColour(wx.ColourDatabase().Find("MAROON"))
        internetBtn.Bind(wx.EVT_BUTTON, self.turnOfInt)

        bmp = wx.Bitmap("power-off.png", wx.BITMAP_TYPE_ANY)
        powerOffBtn = AB.AquaButton(self, bitmap=bmp, label="Turn of computers")
        powerOffBtn.SetForegroundColour(wx.WHITE)
        powerOffBtn.SetBackgroundColour(wx.BLACK)
        powerOffBtn.Bind(wx.EVT_BUTTON, self.turnOfComp)

        bmp = wx.Bitmap("sharing.png", wx.BITMAP_TYPE_ANY)
        shareScreenBtn = AB.AquaButton(self, bitmap=bmp, label="Share screen")
        shareScreenBtn.SetForegroundColour("black")
        shareScreenBtn.SetBackgroundColour(wx.BLUE)
        shareScreenBtn.Bind(wx.EVT_BUTTON, self.turnOfInt)

        bmp = wx.Bitmap("chatt.png", wx.BITMAP_TYPE_ANY)
        internetBtn = AB.AquaButton(self, bitmap=bmp, label="Turn of internet")
        internetBtn.SetForegroundColour(wx.BLACK)
        internetBtn.SetBackgroundColour(wx.ColourDatabase().Find("MAROON"))
        internetBtn.Bind(wx.EVT_BUTTON, self.turnOfInt)



        tools_set = wx.BoxSizer(wx.HORIZONTAL)
        tools_set.Add(powerOffBtn, 0, wx.LEFT, 5)
        tools_set.AddSpacer(40)
        tools_set.Add(internetBtn, 0, wx.RIGHT, 5)
        tools_set.AddSpacer(40)
        tools_set.Add(shareScreenBtn, 0, wx.CENTER, 5)
        #tools_set.AddSpacer()
        v_box.Add(tools_set, 0, wx.CENTER | wx.TOP, 5)
        # v_box.AddSpacer(10)
        #v_box.Add(powerOffBtn, 0, wx.CENTER | wx.ALL, 5)
        v_box.Add(title, 0, wx.CENTER | wx.TOP, 5)
        v_box.AddSpacer(20)
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

    def turnOfInt(self, event):
        """

        :param event:
        :return:
        """
        pass

    def turnOfComp(self, event):
        """

        :param event:
        :return:
        """
        pass


ex = wx.App()
MyFrame(None)
ex.MainLoop()