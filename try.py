import wx
import wx.lib.agw.aquabutton as AB


########################################################################
class MyForm(wx.Frame):

    # ----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "AquaButton Tutorial")
        panel = wx.Panel(self, wx.ID_ANY)
        """
        bmp = wx.Bitmap("agt_mp3.png", wx.BITMAP_TYPE_ANY)
        button = AB.AquaButton(panel, bitmap=bmp, label="Press Me")
        button.SetForegroundColour("black")
        button.Bind(wx.EVT_BUTTON, self.onButton)
        """
        #buttonTwo = AB.AquaButton(panel, label="PulseOnFocus")
        #buttonTwo.SetForegroundColour("white")
        #buttonTwo.SetBackgroundColour(wx.ColourDatabase().Find("VIOLET RED"))

        loginBtn = AB.AquaButton(self, label="login", size=(100, 40))
        loginBtn.SetForegroundColour(wx.WHITE)
        loginBtn.SetBackgroundColour(wx.ColourDatabase().Find("VIOLET RED"))
        loginBtn.SetShadowColor(wx.LIGHT_GREY)
        #buttonTwo.SetDoubleBuffered(self, on= True)
        #buttonTwo.SetPulseOnFocus(True)

        sizer = wx.BoxSizer(wx.VERTICAL)
        #sizer.Add(button, 0, wx.CENTER | wx.ALL, 5)
        sizer.Add(loginBtn, 0, wx.CENTER | wx.ALL, 5)
        panel.SetSizer(sizer)

    # ----------------------------------------------------------------------
    def onButton(self, event):
        """
        This method is fired when its corresponding button is pressed
        """
        message = "You pressed the button!"
        dlg = wx.MessageDialog(None, message, 'Message',
                               wx.OK | wx.ICON_EXCLAMATION)
        dlg.ShowModal()
        dlg.Destroy()


# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()