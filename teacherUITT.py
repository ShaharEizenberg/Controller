import wx
import wx.lib.agw.aquabutton as AB
import wx.lib.scrolledpanel as scrolled
from pubsub import pub

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
        self.chat = ChatBox(self, self.frame)
        # add the panels
        v_box.Add(self.login)
        v_box.Add(self.ui)
        v_box.Add(self.chat)

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
        # connect the pubsub
        #pub.subscribe(self.handle_student_login, "studentLogin")

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
        v_box.AddSpacer(80)
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

    #def handle_student_login(self, position):


class MyPopupMenu(wx.Menu):

    def __init__(self, parent):
        super(MyPopupMenu, self).__init__()

        self.parent = parent

        mmi = wx.MenuItem(self, 1, 'Online')
        self.Append(mmi)
        self.Bind(wx.EVT_MENU, self.OnMinimize, mmi)

        cmi = wx.MenuItem(self, 2, 'Close')
        self.Append(cmi)
        self.Bind(wx.EVT_MENU, self.OnClose, cmi)

    def OnChangeStatus(self, e):
        if self.IsEnabled(1):
            self.Enable(1, False)
        else:
            self.Enable(1, True)

    def OnMinimize(self, e):
        print(self.GetLabel(1))
        if self.GetLabel(1) == "Online":
            self.SetLabel(1, "Offline")
        else:
            self.SetLabel(1, "Online")
        #self.parent.Iconize()

    def OnClose(self, e):
        print(self.GetLabel(1))
        if self.GetLabel(1) == "Online":
            self.SetLabel(1, "Offline")
        else:
            self.SetLabel(1, "Online")


class TeacherUI(wx.Panel):
    """

    """

    def __init__(self, parent, frame):
        wx.Panel.__init__(self, parent, pos=wx.DefaultPosition, size=(1920, 1080), style=wx.SIMPLE_BORDER)
        self.frame = frame
        self.parent = parent
        self.SetBackgroundColour(wx.Colour(47, 48, 56))
        # self.SetBackgroundColour(wx.BLUE)
        self.v_box = wx.BoxSizer(wx.VERTICAL)
        # publish subscribers:
        pub.subscribe(self.handle_student_login, "studentLogin")
        pub.subscribe(self.handle_student_exit, "student exit")

        # the students list
        self.stuList = []
        # connect the pubsub
        #pub.subscribe(self.handle_student_login, "studentLogin")

        # Title
        title = wx.StaticText(self, -1, label="Hello -------")
        titlefont = wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        title.SetForegroundColour(wx.WHITE)
        title.SetFont(titlefont)

        # Toolbar
        self.toolBar = wx.ToolBar(self, style= wx.TB_BOTTOM)
        #self.toolBar.SetBackgroundStyle(wx.TB_BOTTOM)
        self.toolBar.SetBackgroundColour(wx.Colour(47, 48, 56)) # wx.LIGHT_GREY) # wx.Colour(39, 40, 46)))
        # toolbar1 = wx.ToolBar(self)

        shutDownBtn = self.toolBar.AddTool(0, 'shut down computers', wx.Bitmap('power-off.png'))
        #tool = wx.Tool

        #toolTip = wx.ToolTip("shut down computers")
        #shutDownBtn.
        #shutDownBtn.SetShortHelp("shut down computers") # .SetHelpText("shut down computers") # SetToolTip("shut down computers")
        self.toolBar.AddSeparator()
        self.toolBar.AddSeparator()

        shutIntBtn = self.toolBar.AddTool(0, 'shut down internet', wx.Bitmap('no-internet.png'))
        shutIntBtn.SetShortHelp("shut down internet")
        #shutDownBtn.SetHelpText("shut down internet")
        self.toolBar.AddSeparator()
        self.toolBar.AddSeparator()

        shareScreenBtn = self.toolBar.AddTool(0, 'share screen', wx.Bitmap('sharing.png'))
        self.toolBar.AddSeparator()
        self.toolBar.AddSeparator()

        chatBtn = self.toolBar.AddTool(0, 'chat', wx.Bitmap('chatt.png'))

        chatBtn.SetShortHelp("shut down computers")

        #shareScreenBtn.SetShortHelp("share screen with students")
        #shutDownBtn.SetHelpText("share screen")



        #shutDownBtn.SetLabel("shut down computers")
        self.toolBar.Realize()

        self.toolBar.Bind(wx.EVT_TOOL, self.shutDownComp, shutDownBtn)
        self.toolBar.Bind(wx.EVT_TOOL, self.shutDownInt, shutIntBtn)
        self.toolBar.Bind(wx.EVT_TOOL, self.shareScreen, shareScreenBtn)
        self.toolBar.Bind(wx.EVT_TOOL, self.onChat, chatBtn)


        self.v_box.Add(self.toolBar, 0, wx.CENTER, 5)
        self.v_box.AddSpacer(10)
        self.v_box.Add(title, 0, wx.CENTER | wx.TOP, 5)
        self.v_box.AddSpacer(20)
        # add students
        students = self.buidClassMap()
        self.v_box.Add(students, 0, wx.CENTER | wx.TOP, 5)
        self.v_box.AddSpacer(20)
        self.SetSizer(self.v_box)
        self.parent.frame.Layout()
        #print(self.v_box.GetItem(2).GetPosition())

        self.popup = MyPopupMenu(self.parent)



    def buidClassMap(self):
        """

        :return:
        """
        # load image button
        popup = MyPopupMenu(self.parent)
        stuImage = wx.Image("student.png")
        stuImage.Rescale(80, 80)
        stuImage = wx.Bitmap(stuImage)
        columns_box = wx.BoxSizer(wx.HORIZONTAL)
        rows_box = wx.BoxSizer(wx.VERTICAL)
        stuNum = 1
        stuMatrix = []
        #self.Bind(wx.EVT_RIGHT_DOWN, lambda event: self.studentOnClick(event,2), self)
        for i in range(4):
            columns_box = wx.BoxSizer(wx.HORIZONTAL)
            stuRow = []
            for j in range(6):
                stuBtn = wx.BitmapButton(self, name="student", size=(90, 90), bitmap=stuImage, style=0)
                stuBtn.SetBackgroundColour(wx.Colour(47, 48, 56))
                #stuBtn.Bind(wx.EVT_RIGHT_DOWN, self.studentOnClick)
                stuRow.append(stuBtn)
                # add the student button to the student list
                self.stuList.append(stuBtn)

                #stuBtn.Bind(wx.EVT_RIGHT_DOWN, lambda event: self.studentOnClick(event,stuMatrix[i][j]), stuBtn)
                stuBtn.Bind(wx.EVT_RIGHT_DOWN, self.studentOnClick)
                #stuBtn.Bind(wx.EVT_CONTEXT_MENUE, )
                columns_box.Add(stuBtn, 0, wx.EXPAND, 5)
                columns_box.AddSpacer(40)
                if j == 2:
                    columns_box.AddSpacer(40)
                stuNum +=1
                #print("col: ", stuBtn.GetPosition())
            rows_box.Add(columns_box, 0, wx.CENTER, 5)
            rows_box.AddSpacer(80)

            if i == 1:
                rows_box.AddSpacer(80)
            stuMatrix.append(stuRow)

        return rows_box

    def handle_student_login(self, pos):
        """

        :param position:
        :return:
        """
        self.stuList[pos].SetBackgroundColour(wx.GREEN)

    def handle_student_exit(self, pos):
        """

        :param position:
        :return:
        """
        self.stuList[pos].SetBackgroundColour(wx.Colour(47, 48, 56))


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

    def studentOnClick(self, event):
        """

        :param event:
        :param stuNum:
        :return:
        """
        #pos = event.GetPosition()
        #pos = self.ScreenToClient(pos)

        self.parent.PopupMenu(self.popup)

    def onChat(self, event):
        """

        :param event:
        :param stuNum:
        :return:
        """
        print("check press")
        #chat_panel = wx.Panel.__init__(self, self.parent, pos=wx.DefaultPosition, size=(1920, 1080), style=wx.SIMPLE_BORDER)
        #self.SetBackgroundColour(wx.WHITE)
        scrollP = scrolled.ScrolledPanel(self.parent, -1, style=wx.TAB_TRAVERSAL | wx.SUNKEN_BORDER, size=(500, 1080))
        scrollP.SetBackgroundColour(wx.WHITE)
        scrollP.SetupScrolling()
        words = "A Quick Brown Insane Fox Jumped Over the Fence and Ziplined to Cover".split()
        self.spSizer = wx.BoxSizer(wx.VERTICAL)
        for word in words:
            text = wx.TextCtrl(scrollP, value=word)
            #text.Bind(wx.EVT_CHILD_FOCUS, self.file_selected)
            self.spSizer.Add(text)
        scrollP.SetSizer(self.spSizer)




class StudentOptions(wx.Menu):
    def __init__(self, parent):
        super(StudentOptions, self).__init__()
        # super(ToolBar, self).__init__()

        # self.toolbar = toolbar
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

class ChatBox(wx.Panel):
    def __init__(self, parent, frame):
        wx.Panel.__init__(self, parent, pos=(1500, 0), size=(400, 1080), style=wx.SIMPLE_BORDER)
        self.frame = frame
        self.parent = parent
        self.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.Show()





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

    def studentOnClick(self, event):
        """

        :param event:
        :param stuNum:
        :return:
        """
        print("check press")
