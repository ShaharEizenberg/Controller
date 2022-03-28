import wx

class MyFrame(wx.Frame):
    def __init__(self, parent=None):
        super(MyFrame, self).__init__(parent, title="login", size=(500,500))
        self.initUI()
    def initUI(self):
        # create status bar
        self.statusbar = self.CreateStatusBar(1)
        # create main panel - to put on the other panels
        self.login = LoginPanel(self)
        self.stuLogin = StudentLoginPanel(self)
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(self.login, 1, wx.EXPAND)
        box.Add(self.stuLogin, 1, wx.EXPAND)
        # arrange the frame
        #self.login.frame.show()
        #self.stuLogin.frame.show()
        self.SetSizer(box)
        self.Layout()
        #self.Show()



class LoginPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.frame = parent
        self.SetBackgroundColour(wx.LIGHT_GREY)
        v_box = wx.BoxSizer(wx.VERTICAL)

        # title
        title = wx.StaticText(self,-1, label="Login Panel")
        titlefont = wx.Font(22, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        title.SetForegroundColour(wx.BLACK)
        title.SetFont(titlefont)

        # username
        nameBox = wx.BoxSizer(wx.HORIZONTAL)
        nameText = wx.StaticText(self, 1, label="UserName: ")
        self.nameField = wx.TextCtrl(self, -1, name="username", size = (150, -1))
        nameBox.Add(nameText, 0, wx.ALL, 5)
        nameBox.Add(self.nameField, 0, wx.ALL, 5)

        # password
        passBox = wx.BoxSizer(wx.HORIZONTAL)
        passText = wx.StaticText(self, 1, label="UserName: ")
        self.passField = wx.TextCtrl(self, -1, name="username", size=(150, -1))
        passBox.Add(passText, 0, wx.ALL, 5)
        passBox.Add(self.passField, 0, wx.ALL, 5)

        btnBox = wx.BoxSizer(wx.HORIZONTAL)
        loginBtn = wx.Button(self, wx.ID_ANY, label="login", size = (100, 40))
        loginBtn.Bind(wx.EVT_BUTTON, self.handle_login)
        btnBox.Add(loginBtn, 0, wx.ALL, 5)


        v_box.Add(title, 0, wx.CENTER | wx.TOP, 5)
        v_box.AddSpacer(10)
        v_box.Add(nameBox, 0, wx.CENTER | wx.ALL, 5)
        v_box.Add(passBox, -1, wx.CENTER | wx.ALL, 5)
        v_box.AddSpacer(10)
        v_box.Add(btnBox, wx.CENTER | wx.ALL, 5)

        # show the panel
        self.frame.show()
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




class StudentLoginPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.frame = parent
        self.SetBackgroundColour(wx.LIGHT_GREY)
        v_box = wx.BoxSizer(wx.VERTICAL)

        # title
        title = wx.StaticText(self,-1, label="Login Panel")
        titlefont = wx.Font(22, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        title.SetForegroundColour(wx.BLACK)
        title.SetFont(titlefont)

        # id
        idBox = wx.BoxSizer(wx.HORIZONTAL)
        idText = wx.StaticText(self, 1, label="UserName: ")
        self.nameField = wx.TextCtrl(self, -1, name="username", size = (150, -1))
        idBox.Add(idText, 0, wx.ALL, 5)
        idBox.Add(self.nameField, 0, wx.ALL, 5)

        btnBox = wx.BoxSizer(wx.HORIZONTAL)
        loginBtn = wx.Button(self, wx.ID_ANY, label="login", size = (100, 40))
        loginBtn.Bind(wx.EVT_BUTTON, self.handle_login)
        btnBox.Add(loginBtn, 0, wx.ALL, 5)


        v_box.Add(title, 0, wx.CENTER | wx.TOP, 5)
        v_box.AddSpacer(10)
        v_box.Add(idBox, 0, wx.CENTER | wx.ALL, 5)
        v_box.AddSpacer(10)
        v_box.Add(btnBox, wx.CENTER | wx.ALL, 5)

        # show the panel
        self.frame.show()
        self.SetSizer(v_box)
        self.Layout()

    def handle_login(self, event):
        """

        :return:
        """
        id = self.nameField.GetValue()
        if id == "":
            self.frame.SetStatusText("Must enter name and password")
        else:
            self.frame.SetStatusText("waiting for Server approve")









ex = wx.App()
MyFrame(None)
ex.MainLoop()
