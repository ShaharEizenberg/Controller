import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        #self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        self.toolbar = self.CreateToolBar()

        # load image button
        upImage = wx.Image("student.png")
        upImage.Rescale(80, 80)
        upImage = wx.Bitmap(upImage)
        upBtn = wx.BitmapButton(self, name="student",  size = (80, 80), bitmap = upImage, style= 0)
        upBtn.SetBackgroundColour(wx.LIGHT_GREY)
        #upBtn.


        wximg = wx.Image("student.png", type=wx.BITMAP_TYPE_ANY)

        td = self.toolbar.AddTool(1, 'right', wx.Bitmap('power-off.png')) # , kind=wx.ITEM_CHECK)
        te = self.toolbar.AddTool(2, 'wrong', wx.Bitmap('no-internet.png'))
        #self.toolbar.AddTool(upBtn)
        self.toolbar.Realize()
        self.toolbar.Bind(wx.EVT_TOOL, self.OnOne, td)

        self.SetSize((400, 400))
        self.SetTitle('Undo redo')
        #self.Centre()


        # tryy

        # title
        title = wx.StaticText(self, -1, label="Hello -------")
        titlefont = wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        title.SetForegroundColour(wx.BLACK)
        title.SetFont(titlefont)


        v_box = wx.BoxSizer(wx.VERTICAL)
        v_box.Add(self.toolbar, 0, wx.EXPAND, 5)
        v_box.AddSpacer(10)
        v_box.Add(title, 0, wx.CENTER | wx.TOP, 5)
        v_box.Add(upBtn, 0, wx.CENTER | wx.CENTER, 5)

        self.SetSizer(v_box)
        self.Layout()

    def OnOne(self, e):
        # Toggle tool using ToggleTool() function
        #self.toolbar.ToggleTool(toolId=1, toggle=True)
        # Realize() called to finalize new added tools
        self.toolbar.Realize()

    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()