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
        self.SetBackgroundColour(wx.ColourDatabase().Find("DIM GREY"))
        # create toolbar
        #self.toolBar = ToolBar(wx.ToolBar())
        # self.SetBackgroundColour(wx.BLUE)
        v_box = wx.BoxSizer(wx.VERTICAL)

        # title
        title = wx.StaticText(self, -1, label="Hello -------")
        titlefont = wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        title.SetForegroundColour(wx.BLACK)
        title.SetFont(titlefont)


        #v_box.Add(menubar, 0, wx.CENTER | wx.TOP, 5)
        # v_box.AddSpacer(10)
        #v_box.Add(powerOffBtn, 0, wx.CENTER | wx.ALL, 5)

        self.toolBar = wx.ToolBar(self.parent.frame)
        # toolbar1 = wx.ToolBar(self)

        shutDownBtn = self.toolBar.AddTool(wx.ID_ANY, '', wx.Bitmap('power-off.png'))
        shutIntBtn = self.toolBar.AddTool(wx.ID_ANY, '', wx.Bitmap('no-internet.png'))
        shareScreenBtn = self.toolBar.AddTool(wx.ID_ANY, '', wx.Bitmap('sharing.png'))
        self.toolBar.Realize()

        self.parent.frame.Bind(wx.EVT_TOOL, self.shutDownComp, shutDownBtn)
        self.parent.frame.Bind(wx.EVT_TOOL, self.shutDownInt, shutIntBtn)
        self.parent.frame.Bind(wx.EVT_TOOL, self.shareScreen, shareScreenBtn)


        v_box.Add(self.toolBar, 0, wx.EXPAND)
        v_box.AddSpacer(10)
        v_box.Add(title, 0, wx.CENTER | wx.TOP, 5)
        v_box.AddSpacer(20)
        #v_box.Add(internetBtn, 0, wx.CENTER | wx.ALL, 5)
        # v_box.AddSpacer(10)
        #v_box.Add(powerOffBtn, 0, wx.CENTER | wx.ALL, 5)

        # show the panel
        # self.Show()
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

    def shutDownInt(self, event):
        """

        :param event:
        :return:
        """
        print("shutDownInt ")
        pass

    def shutDownComp(self, event):
        """

        :param event:
        :return:
        """
        print("shutDownComp")
        pass

    def shareScreen(self, event):
        """

        :param event:
        :return:
        """
        print("shareScreen")
        pass


class MenuBar(wx.ToolBar):
    def __init__(self, toolbar):
        #super(ToolBar, self).__init__()

        #self.toolbar = toolbar
        # shut down computers button
        powerOffBtn = wx.MenuItem(self, wx.NewId(), "&Shut down computers")
        powerOffBtn.SetBitmap(wx.Bitmap("power-off.png"))
        self.AddTool(powerOffBtn)
        self.Bind(wx.EVT_MENU, self.shutDownComp, powerOffBtn)

        # shut down internet button
        shutInternetBtn = wx.MenuItem(self, wx.NewId(), "&Shut down internet")
        shutInternetBtn.SetBitmap(wx.Bitmap("no-internet.png"))
        self.AddTool(shutInternetBtn)
        self.Bind(wx.EVT_MENU, self.shutDownInt, powerOffBtn)

        # share screen button
        shareScreenBtn = wx.MenuItem(self, wx.NewId(), "&Share screen")
        shareScreenBtn.SetBitmap(wx.Bitmap("sharing.png"))
        self.AddTool(shareScreenBtn)
        self.Bind(wx.EVT_MENU, self.shareScreen, powerOffBtn)


class ToolBar(wx.ToolBar):
    def __init__(self, toolbar):
        super(ToolBar, self).__init__()

        self.toolbar = toolbar
        #toolbar1 = wx.ToolBar(self)
        self.toolbar.AddTool(wx.ID_ANY, '', wx.Bitmap('power-off.png'))
        self.toolbar.AddTool(wx.ID_ANY, '', wx.Bitmap('no-internet.png'))
        self.toolbar.AddTool(wx.ID_ANY, '', wx.Bitmap('sharing.png'))
        self.toolbar.Realize()

        """
        self.parent = parent
        # shut down computers button
        powerOffBtn = wx.MenuItem(self, wx.NewId(), "&Shut down computers")
        powerOffBtn.SetBitmap(wx.Bitmap("power-off.png"))
        self.AddTool(powerOffBtn)
        self.Bind(wx.EVT_MENU, self.shutDownComp, powerOffBtn)

        # shut down internet button
        shutInternetBtn = wx.MenuItem(self, wx.NewId(), "&Shut down internet")
        shutInternetBtn.SetBitmap(wx.Bitmap("no-internet.png"))
        self.AddTool(shutInternetBtn)
        self.Bind(wx.EVT_MENU, self.shutDownInt, powerOffBtn)

        # share screen button
        shareScreenBtn = wx.MenuItem(self, wx.NewId(), "&Share screen")
        shareScreenBtn.SetBitmap(wx.Bitmap("sharing.png"))
        self.AddTool(shareScreenBtn)
        self.Bind(wx.EVT_MENU, self.shareScreen, powerOffBtn)
        
        """





        """
        mmi = wx.MenuItem(self, wx.NewId(), 'Minimize')
        self.Append(mmi)
        self.Bind(wx.EVT_MENU, self.OnMinimize, mmi)

        cmi = wx.MenuItem(self, wx.NewId(), 'Close')
        self.Append(cmi)
        self.Bind(wx.EVT_MENU, self.OnClose, cmi)
        """

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

    def shutDownInt(self, event):
        """

        :param event:
        :return:
        """
        pass

    def shutDownComp(self, event):
        """

        :param event:
        :return:
        """
        pass

    def shareScreen(self, event):
        """

        :param event:
        :return:
        """
        pass


ex = wx.App()
MyFrame(None)
ex.MainLoop()