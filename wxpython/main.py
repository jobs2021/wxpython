import wx

class ventana(wx.Frame):
    def __init__(self,parent,title):
        super(ventana,self).__init__(parent,title=title,size=(300,230))
        self.Show()
        self.Center()
        self.initUI()

    def initUI(self):
        #crear panel
        panel=wx.Panel(self)

        #agregar img
        img=wx.Image("Google.jpg",wx.BITMAP_TYPE_ANY)
        img=img.Scale(img.GetWidth()/5,img.GetHeight()/5)
        sbitmap=wx.StaticBitmap(panel,-1,wx.Bitmap(img))

        #crear controles
        txt_user=wx.TextCtrl(panel,value="usuario",style=wx.TE_CENTER,size=(200,30))
        txt_password=wx.TextCtrl(panel,value="usuario",style=wx.TE_CENTER|wx.TE_PASSWORD,size=(200,30))
        btn_login=wx.Button(panel,label="Inciar Sesion",size=(200,30))

        #crear sizer
        bs=wx.BoxSizer(wx.VERTICAL)

        #agregar elementos al sizer
        bs.Add(sbitmap, 0, flag=wx.ALL | wx.CENTER, border=5)
        bs.Add(txt_user,0,flag=wx.ALL|wx.CENTER,border=5)
        bs.Add(txt_password, 0, flag=wx.ALL | wx.CENTER, border=5)
        bs.Add(btn_login, 0, flag=wx.ALL | wx.CENTER, border=5)

        #setear el sizer al panel
        panel.SetSizer(bs)

        #agregar evento al boton login
        btn_login.Bind(wx.EVT_BUTTON,lambda event: self.login(event,txt_user.GetValue(),txt_password.GetValue()))




     #metodo para logearse
    def login(self,event,user,password):
        import pypyodbc
        con=pypyodbc.connect("Driver={ODBC Driver 17 for SQL Server};server=localhost;database=db;uid=sa;pwd=YOUR_PASSWORD")
        cursor=con.cursor()
        query=f"select nombre,contra from usuarios where nombre='{user}' and contra='{password}'"
        resultado=cursor.execute(query).fetchall()
        con.close()

        #creamos un try catch para capturar errores

        try:
            usuario=resultado[0][0] #primer resultado[0], [0] posicion del valor del nombre
            wx.MessageBox("Bienvenido "+usuario)

        except:
            wx.MessageBox("Usuario o contraseña invalidos")





if __name__=="__main__":
    app=wx.App()
    v=ventana(None,"WXPYTHON")
    app.MainLoop()
