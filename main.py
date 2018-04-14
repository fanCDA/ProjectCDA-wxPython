import wx

class MyFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "Hello World", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_scrolledWindow = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.VSCROLL )
		self.m_scrolledWindow.SetScrollRate( 5, 5 )
		gSizer = wx.GridSizer( 0, 8, 0, 0 )

		for x in range(100):
		
                    textCtrl = wx.TextCtrl( self.m_scrolledWindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
                    
                    textCtrl.SetMinSize( wx.Size( 1,150 ) )
                    textCtrl.SetMaxSize( wx.Size( -1,150 ) )
                    
                    gSizer.Add( textCtrl, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_scrolledWindow.SetSizer( gSizer )
		self.m_scrolledWindow.Layout()
		gSizer.Fit( self.m_scrolledWindow )
		bSizer.Add( self.m_scrolledWindow, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()
