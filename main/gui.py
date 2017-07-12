import blisscribe

try:
    import wx
except ImportError:
    raise(ImportError, "You need to download the wxPython module to run this program.")


class blissApp(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        self.parent = parent
        self.dims = (1000, 500)
        self.textMode()

    def initialize(self):
        menuBar = wx.MenuBar()
        filemenu = wx.Menu()

        toTranslate = filemenu.Append(wx.ID_ANY, "Translate", " Translate the input text")
        menuBar.Append(filemenu, "&Menu")

        self.Bind(wx.EVT_MENU, self.onTranslate, toTranslate)

        self.SetMenuBar(menuBar)  # sets this frame's menu bar

        self.SetSize(self.dims)
        self.Centre()
        self.Show(True)

    def onTranslate(self, event):
        print("You pressed translate! ")
        self.blissMode()

    def textMode(self):
        """
        The default mode of this translator, where users can (indefinitely) type
        English text to be translated to Blissymbols.
        """
        self.entry = wx.TextCtrl(self, -1, value="Enter text to translate here. ")
        self.initialize()

    def blissMode(self):
        """
        The special mode of this translator, where users can view a combination
        of (rendered) English words and translated Blissymbols.
        """
        screen = wx.ScreenDC()
        brush = wx.Brush("white")
        screen.SetBackground(brush)
        screen.Clear()

        # TODO: replace dummy input text with fetched user input
        pages = blisscribe.translate("user's input text")
        bmps = []
        idx = 1

        for page in pages:
            # TODO: render at least the first image in Blisscribe pages
            # TODO: add page-turning handler for multi-page translations
            filename = str(idx) + ".bmp"
            page.save(filename, "BMP")
            img = blisscribe.Image.open(filename)
            img = wx.BitmapFromImage(img)
            bmps.append(img)

        for bmp in bmps:
            screen.DrawBitmap(bmp)

        self.initialize()


if __name__ == "__main__":
    app = wx.App()
    frame = blissApp(None, -1, 'Blisscribe')
    app.MainLoop()

"""
class blissApp(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.initialize()

    def initialize(self):
        row_minsize = 20
        row_idx = 0
        self.entry = Tkinter.Entry(self)
        self.entry.grid(column=0, row=0, sticky="NW")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(row_idx, minsize=row_minsize, weight=1)

        if self.height > row_minsize:
            row_idx += 1
            self.grid_rowconfigure(row_idx, minsize=row_minsize, weight=1)

        #num_rows = self.entry.grid_size()[1]
        #for i in range(0, num_rows + 1):
        #    self.grid_rowconfigure(i, weight=1)
        #self.entry.rowconfigure(0, weight=1)
        #print(self.entry.grid_size())

if __name__ == "__main__":
    app = blissApp(None)
    app.title("Blisscribe")
    app.mainloop()


class TextFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title, size=(1000,500))
        self.parent = parent
        self.InitUI()

    def InitUI(self):
        self.MakeUI()
        self.Show(True)

    def MakeUI(self):
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        # Creating the menubar.
        menuBar = wx.MenuBar()
        filemenu = wx.Menu()

        #filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        #filemenu.AppendSeparator()
        #filemenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")
        #filemenu.AppendSeparator()

        toTranslate = filemenu.Append(wx.ID_ANY, "Translate", " Translate the input text")
        filemenu.AppendSeparator()
        toQuit = filemenu.Append(wx.ID_EXIT, "Quit", "Quit application")

        menuBar.Append(filemenu, "&Menu") # Adding the "filemenu" to the MenuBar

        self.Bind(wx.EVT_MENU, self.OnTranslate, toTranslate)
        self.Bind(wx.EVT_MENU, self.OnQuit, toQuit)

        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        self.SetSize((1000, 500))
        self.SetTitle("Blisscribe")
        self.Centre()

    def OnTranslate(self, event):
        pages = blisscribe.translate("Input text")
        png = wx.Image(pages[-1].save(blisscribe.IMG_PATH + "1", format="PNG"), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png, (10, 5), (png.GetWidth(), png.GetHeight()))
        self.InitTranslation()

        '''
        idx = 1

        for page in pages:
            png = wx.Image(page.save(blisscribe.IMG_PATH + idx), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            wx.StaticBitmap(self, -1, png, (10, 5), (png.GetWidth(), png.GetHeight()))
            idx += 1
        '''
        # TODO: on click (of button?), render next page in pages (once pages are done being read, start over(?))

    def InitTranslation(self):
        wx.Frame.Destroy()
        # TODO: create new frame with Blissymbol translated pages inside of it


    def OnQuit(self, event):
        self.Close()
"""
