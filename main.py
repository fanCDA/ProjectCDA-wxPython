import wx


class MyFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="Hello World", pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.VSCROLL)
        self.m_scrolledWindow.SetScrollRate(5, 5)
        gSizer = wx.GridSizer(0, 8, 0, 0)

        for x in range(100):
            bSizer4 = wx.BoxSizer(wx.VERTICAL)
            bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

            self.m_staticText1 = wx.StaticText(self.m_scrolledWindow, wx.ID_ANY, u"MyLabel", wx.DefaultPosition,
                                               wx.DefaultSize, wx.ALIGN_LEFT)
            self.m_staticText1.Wrap(-1)
            self.m_staticText1.SetMinSize(wx.Size(1, -1))
            bSizer5.Add(self.m_staticText1, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 5)

            self.m_staticText2 = wx.StaticText(self.m_scrolledWindow, wx.ID_ANY, u"MyLabel", wx.DefaultPosition,
                                               wx.DefaultSize, wx.ALIGN_RIGHT)
            self.m_staticText2.Wrap(-1)
            self.m_staticText2.SetMinSize(wx.Size(1, -1))
            bSizer5.Add(self.m_staticText2, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, 5)

            bSizer4.Add(bSizer5, 0, wx.EXPAND, 5)

            self.m_textCtrl11 = wx.TextCtrl(self.m_scrolledWindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
            self.m_textCtrl11.SetMinSize(wx.Size(1, -1))
            bSizer4.Add(self.m_textCtrl11, 0, wx.ALL | wx.EXPAND, 5)

            bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

            self.m_textCtrl12 = wx.TextCtrl(self.m_scrolledWindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
            self.m_textCtrl12.SetMinSize(wx.Size(1, 150))
            self.m_textCtrl12.SetMaxSize(wx.Size(-1, 150))

            bSizer6.Add(self.m_textCtrl12, 1, wx.ALL | wx.EXPAND, 5)

            self.m_textCtrl13 = wx.TextCtrl(self.m_scrolledWindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
            self.m_textCtrl13.SetMinSize(wx.Size(1, 150))
            self.m_textCtrl13.SetMaxSize(wx.Size(-1, 150))

            bSizer6.Add(self.m_textCtrl13, 1, wx.ALL | wx.EXPAND, 5)

            bSizer4.Add(bSizer6, 1, wx.EXPAND, 5)

            gSizer.Add(bSizer4, 0, wx.ALL | wx.EXPAND, 5)

        self.m_scrolledWindow.SetSizer(gSizer)
        self.m_scrolledWindow.Layout()
        gSizer.Fit(self.m_scrolledWindow)
        bSizer.Add(self.m_scrolledWindow, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()
