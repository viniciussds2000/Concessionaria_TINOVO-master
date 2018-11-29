from tkinter import *


class Carros(Tk):
    def __init__(self):
        super().__init__()

        self.font = ('Verdana', '14', 'bold')
        self.font2 = ('Verdana','10','bold')

        self['bg'] = 'gray14'
        self.geometry('400x400+750+100')
        self.title('Concessionária - CARROS')

        self.bt1 = Button(self, width=11, height=5, text="Bmw X5", bg = 'gold',font = self.font2, command=Bmw)
        self.bt2 = Button(self, width=11, height=5, text="New Civic", bg = 'gold',font = self.font2, command=Civic)
        self.bt3 = Button(self, width=11, height=5, text="Audi A7", bg='gold',font = self.font2, command=Audi)
        self.bt4 = Button(self, width=11, height=5, text="Camaro", bg='gold',font = self.font2, command=Camaro)
        self.bt5 = Button(self, width=11, height=5, text="Mustang", bg='gold',font = self.font2, command=Mustang)
        self.bt6 = Button(self, width=11, height=5, text="Porsche", bg='gold', font=self.font2, command=Porsche)

        self.lb = Label(self ,text='PÁTIO',bg='gray14',fg='cyan2' ,font = self.font)
        self.lb.place(x=160, y=20)
        self.lb2 = Label(self, text='ESCOLHA O CARRO',bg = 'gray14',fg = 'gray99', font = self.font2)
        self.lb2.place(x=25,y=70)

        self.bt1.place(x=25, y=100)
        self.bt2.place(x=145, y=100)
        self.bt3.place(x=265, y=100)
        self.bt4.place(x=25, y=240)
        self.bt5.place(x=145, y=240)
        self.bt6.place(x=265,y=240)
#=============================================================================================================================
class Bmw(Toplevel):
    def __init__(self):
        super().__init__()

        self['bg'] = 'gray14'
        self.geometry('400x400+750+100')
        self.title('Detalhes da Compra')
        self.font = ('Verdana', '16', 'bold')
        self.font2 = ('Verdana', '11')

        self.lb = Label(self, text='DADOS FINAIS!', bg='gray14', fg='cyan2', font=self.font)
        self.lb.place(x=100, y=30)
        self.lb2 = Label(self, text='Nome do vendedor:', bg='gray14', fg='white', font=self.font2)
        self.lb2.place(x=7, y=100)
        self.lb3 = Label(self, text='Nome do Cliente:', bg='gray14', fg='white', font=self.font2)
        self.lb3.place(x=7, y=130)
        self.lb4 = Label(self, text='Data da compra:', bg='gray14', fg='white', font=self.font2)
        self.lb4.place(x=7, y=300)
        self.valor = Label(self, text='VALOR DE VENDA:',bg='gray14',fg='white',font=self.font)
        self.valor.place(x=7,y=193)
        # entrys
        self.ed1 = Entry(self, width=20)
        self.ed1.place(x=165, y=104)
        self.ed2 = Entry(self, width=23)
        self.ed2.place(x=146, y=133)
        self.ed3 = Entry(self, width=10)
        self.ed3.place(x=140, y=305)
        self.ed4 = Entry(self, width=15)
        self.ed4.place(x=225,y=200)
        # botao confirm
        self.bt = Button(self, width=10, height=3, bg='lime green', text='Continuar', command = self.bmwaba)
        self.bt.place(x=300, y=320)
 #-------------------
    def bmwaba(self):
        super().__init__()

        self.geometry("400x400+750+100")
        self.title("NOTA")
        self["bg"] = 'gray14'
        self.font = ('Verdana', '18', 'bold')
        self.font2 = ('Gotham', '16', 'italic')
        self.font3 = ('Verdana', '11')
        self.font4 = ('Verdana', '16', 'bold')
        self.font5 = ('Gotham','16','bold')

        self.lb = Label(self, text='Compra efetuada!', bg='gray14', fg='white', font=self.font)
        self.lb.place(x=20, y=15)
        self.lb2 = Label(self, text='Bmw X5 2015               R$302.500', bg='gray14', fg='yellow2', font=self.font2)
        self.lb2.place(x=18, y=80)
        self.lb3 = Label(self, text='Comprador:', bg='gray14', fg='red2', font=self.font3)
        self.lb3.place(x=18, y=150)
        self.lb4 = Label(self, text='Vendedor:', bg='gray14', fg='red2', font=self.font3)
        self.lb4.place(x=18, y=190)
        self.lb5 = Label(self, text='Data de compra:', bg='gray14', fg='red2', font=self.font3)
        self.lb5.place(x=18, y=290)
        self.lb6 = Label(self, text='Valor:R$', bg='gray14', fg='white', font=self.font5)
        self.lb6.place(x=200, y=360)

        self.nomevendedor = Label(self,text = self.ed2.get(),bg = 'gray14',fg='white',font=self.font5)
        self.nomevendedor.place(x=115,y=150)
        self.nomecliente = Label(self,text=self.ed1.get(),bg='gray14',fg='white',font=self.font5)
        self.nomecliente.place(x=100,y=190)
        self.datacompra = Label(self, text = self.ed3.get(),bg = 'gray14',fg='white', font=self.font5)
        self.datacompra.place(x=150,y=290)
        self.valorvenda = Label(self,text = self.ed4.get(),bg = 'gray14',fg='yellow', font=self.font5)
        self.valorvenda.place(x=290,y=360)

#---------------------------------------------------------------------------------------------------------------------
class Civic(Toplevel):
    def __init__(self):
        super().__init__()
        self['bg'] = 'gray14'
        self.geometry('400x400+750+100')
        self.title('Detalhes da Compra')
        self.font = ('Verdana', '16', 'bold')
        self.font2 = ('Verdana', '11')

        self.lb = Label(self, text='DADOS FINAIS!', bg='gray14', fg='cyan2', font=self.font)
        self.lb.place(x=100, y=30)
        self.lb2 = Label(self, text='Nome do vendedor:', bg='gray14', fg='white', font=self.font2)
        self.lb2.place(x=7, y=100)
        self.lb3 = Label(self, text='Nome do Cliente:', bg='gray14', fg='white', font=self.font2)
        self.lb3.place(x=7, y=130)
        self.lb4 = Label(self, text='Data da compra:', bg='gray14', fg='white', font=self.font2)
        self.lb4.place(x=7, y=300)
        self.valor = Label(self, text='VALOR DE VENDA:', bg='gray14', fg='white', font=self.font)
        self.valor.place(x=7, y=193)
        # entrys
        self.ed1 = Entry(self, width=20)
        self.ed1.place(x=165, y=104)
        self.ed2 = Entry(self, width=23)
        self.ed2.place(x=146, y=133)
        self.ed3 = Entry(self, width=10)
        self.ed3.place(x=140, y=305)
        self.ed4 = Entry(self, width=15)
        self.ed4.place(x=225, y=200)
        # botao confirm
        self.bt = Button(self, width=10, height=3, bg='lime green', text='Continuar', command=self.civicaba)
        self.bt.place(x=300, y=320)

    # -------------------
    def civicaba(self):
        super().__init__()

        self.geometry("400x400+750+100")
        self.title("NOTA")
        self["bg"] = 'gray14'
        self.font = ('Verdana', '18', 'bold')
        self.font2 = ('Gotham', '16', 'italic')
        self.font3 = ('Verdana', '11')
        self.font4 = ('Verdana', '16', 'bold')
        self.font5 = ('Gotham', '16', 'bold')

        self.lb = Label(self, text='Compra efetuada!', bg='gray14', fg='white', font=self.font)
        self.lb.place(x=20, y=15)
        self.lb2 = Label(self, text='New Civic 2018               R$105.000 ', bg='gray14', fg='yellow2', font=self.font2)
        self.lb2.place(x=18, y=80)
        self.lb3 = Label(self, text='Comprador:', bg='gray14', fg='red2', font=self.font3)
        self.lb3.place(x=18, y=150)
        self.lb4 = Label(self, text='Vendedor:', bg='gray14', fg='red2', font=self.font3)
        self.lb4.place(x=18, y=190)
        self.lb5 = Label(self, text='Data de compra:', bg='gray14', fg='red2', font=self.font3)
        self.lb5.place(x=18, y=290)
        self.lb6 = Label(self, text='Valor:R$', bg='gray14', fg='white', font=self.font5)
        self.lb6.place(x=200, y=360)

        self.nomevendedor = Label(self, text=self.ed2.get(), bg='gray14', fg='white', font=self.font5)
        self.nomevendedor.place(x=115, y=150)
        self.nomecliente = Label(self, text=self.ed1.get(), bg='gray14', fg='white', font=self.font5)
        self.nomecliente.place(x=100, y=190)
        self.datacompra = Label(self, text=self.ed3.get(), bg='gray14', fg='white', font=self.font5)
        self.datacompra.place(x=150, y=290)
        self.valorvenda = Label(self, text=self.ed4.get(), bg='gray14', fg='yellow', font=self.font5)
        self.valorvenda.place(x=290, y=360)


#-------------------------------------------------------------------------------------------------------------------
class Audi(Toplevel):
    def __init__(self):
        super().__init__()
        self['bg'] = 'gray14'
        self.geometry('400x400+750+100')
        self.title('Detalhes da Compra')
        self.font = ('Verdana', '16', 'bold')
        self.font2 = ('Verdana', '11')

        self.lb = Label(self, text='DADOS FINAIS!', bg='gray14', fg='cyan2', font=self.font)
        self.lb.place(x=100, y=30)
        self.lb2 = Label(self, text='Nome do vendedor:', bg='gray14', fg='white', font=self.font2)
        self.lb2.place(x=7, y=100)
        self.lb3 = Label(self, text='Nome do Cliente:', bg='gray14', fg='white', font=self.font2)
        self.lb3.place(x=7, y=130)
        self.lb4 = Label(self, text='Data da compra:', bg='gray14', fg='white', font=self.font2)
        self.lb4.place(x=7, y=300)
        self.valor = Label(self, text='VALOR DE VENDA:', bg='gray14', fg='white', font=self.font)
        self.valor.place(x=7, y=193)
        # entrys
        self.ed1 = Entry(self, width=20)
        self.ed1.place(x=165, y=104)
        self.ed2 = Entry(self, width=23)
        self.ed2.place(x=146, y=133)
        self.ed3 = Entry(self, width=10)
        self.ed3.place(x=140, y=305)
        self.ed4 = Entry(self, width=15)
        self.ed4.place(x=225, y=200)
        # botao confirm
        self.bt = Button(self, width=10, height=3, bg='lime green', text='Continuar', command=self.audiaba)
        self.bt.place(x=300, y=320)

    # -------------------
    def audiaba(self):
        super().__init__()

        self.geometry("400x400+750+100")
        self.title("NOTA")
        self["bg"] = 'gray14'
        self.font = ('Verdana', '18', 'bold')
        self.font2 = ('Gotham', '16', 'italic')
        self.font3 = ('Verdana', '11')
        self.font4 = ('Verdana', '16', 'bold')
        self.font5 = ('Gotham', '16', 'bold')

        self.lb = Label(self, text='Compra efetuada!', bg='gray14', fg='white', font=self.font)
        self.lb.place(x=20, y=15)
        self.lb2 = Label(self, text='Audi A7 2018               R$425.900 ', bg='gray14', fg='yellow2', font=self.font2)
        self.lb2.place(x=18, y=80)
        self.lb3 = Label(self, text='Comprador:', bg='gray14', fg='red2', font=self.font3)
        self.lb3.place(x=18, y=150)
        self.lb4 = Label(self, text='Vendedor:', bg='gray14', fg='red2', font=self.font3)
        self.lb4.place(x=18, y=190)
        self.lb5 = Label(self, text='Data de compra:', bg='gray14', fg='red2', font=self.font3)
        self.lb5.place(x=18, y=290)
        self.lb6 = Label(self, text='Valor:R$', bg='gray14', fg='white', font=self.font5)
        self.lb6.place(x=200, y=360)

        self.nomevendedor = Label(self, text=self.ed2.get(), bg='gray14', fg='white', font=self.font5)
        self.nomevendedor.place(x=115, y=150)
        self.nomecliente = Label(self, text=self.ed1.get(), bg='gray14', fg='white', font=self.font5)
        self.nomecliente.place(x=100, y=190)
        self.datacompra = Label(self, text=self.ed3.get(), bg='gray14', fg='white', font=self.font5)
        self.datacompra.place(x=150, y=290)
        self.valorvenda = Label(self, text=self.ed4.get(), bg='gray14', fg='yellow', font=self.font5)
        self.valorvenda.place(x=290, y=360)
#---------------------------------------------------------------------------------------------------------------
class Camaro(Toplevel):
    def __init__(self):
        super().__init__()
        self['bg'] = 'gray14'
        self.geometry('400x400+750+100')
        self.title('Detalhes da Compra')
        self.font = ('Verdana', '16', 'bold')
        self.font2 = ('Verdana', '11')

        self.lb = Label(self, text='DADOS FINAIS!', bg='gray14', fg='cyan2', font=self.font)
        self.lb.place(x=100, y=30)
        self.lb2 = Label(self, text='Nome do vendedor:', bg='gray14', fg='white', font=self.font2)
        self.lb2.place(x=7, y=100)
        self.lb3 = Label(self, text='Nome do Cliente:', bg='gray14', fg='white', font=self.font2)
        self.lb3.place(x=7, y=130)
        self.lb4 = Label(self, text='Data da compra:', bg='gray14', fg='white', font=self.font2)
        self.lb4.place(x=7, y=300)
        self.valor = Label(self, text='VALOR DE VENDA:', bg='gray14', fg='white', font=self.font)
        self.valor.place(x=7, y=193)
        # entrys
        self.ed1 = Entry(self, width=20)
        self.ed1.place(x=165, y=104)
        self.ed2 = Entry(self, width=23)
        self.ed2.place(x=146, y=133)
        self.ed3 = Entry(self, width=10)
        self.ed3.place(x=140, y=305)
        self.ed4 = Entry(self, width=15)
        self.ed4.place(x=225, y=200)
        # botao confirm
        self.bt = Button(self, width=10, height=3, bg='lime green', text='Continuar', command=self.camaroaba)
        self.bt.place(x=300, y=320)

    # -------------------
    def camaroaba(self):
        super().__init__()

        self.geometry("400x400+750+100")
        self.title("NOTA")
        self["bg"] = 'gray14'
        self.font = ('Verdana', '18', 'bold')
        self.font2 = ('Gotham', '16', 'italic')
        self.font3 = ('Verdana', '11')
        self.font4 = ('Verdana', '16', 'bold')
        self.font5 = ('Gotham', '16', 'bold')

        self.lb = Label(self, text='Compra efetuada!', bg='gray14', fg='white', font=self.font)
        self.lb.place(x=20, y=15)
        self.lb2 = Label(self, text='Camaro 2017               R$370.990 ', bg='gray14', fg='yellow2', font=self.font2)
        self.lb2.place(x=18, y=80)
        self.lb3 = Label(self, text='Comprador:', bg='gray14', fg='red2', font=self.font3)
        self.lb3.place(x=18, y=150)
        self.lb4 = Label(self, text='Vendedor:', bg='gray14', fg='red2', font=self.font3)
        self.lb4.place(x=18, y=190)
        self.lb5 = Label(self, text='Data de compra:', bg='gray14', fg='red2', font=self.font3)
        self.lb5.place(x=18, y=290)
        self.lb6 = Label(self, text='Valor:R$', bg='gray14', fg='white', font=self.font5)
        self.lb6.place(x=200, y=360)

        self.nomevendedor = Label(self, text=self.ed2.get(), bg='gray14', fg='white', font=self.font5)
        self.nomevendedor.place(x=115, y=150)
        self.nomecliente = Label(self, text=self.ed1.get(), bg='gray14', fg='white', font=self.font5)
        self.nomecliente.place(x=100, y=190)
        self.datacompra = Label(self, text=self.ed3.get(), bg='gray14', fg='white', font=self.font5)
        self.datacompra.place(x=150, y=290)
        self.valorvenda = Label(self, text=self.ed4.get(), bg='gray14', fg='yellow', font=self.font5)
        self.valorvenda.place(x=290, y=360)
#-----------------------------------------------------------------------------------------------------------
class Mustang(Toplevel):
    def __init__(self):
        super().__init__()
        self['bg'] = 'gray14'
        self.geometry('400x400+750+100')
        self.title('Detalhes da Compra')
        self.font = ('Verdana', '16', 'bold')
        self.font2 = ('Verdana', '11')

        self.lb = Label(self, text='DADOS FINAIS!', bg='gray14', fg='cyan2', font=self.font)
        self.lb.place(x=100, y=30)
        self.lb2 = Label(self, text='Nome do vendedor:', bg='gray14', fg='white', font=self.font2)
        self.lb2.place(x=7, y=100)
        self.lb3 = Label(self, text='Nome do Cliente:', bg='gray14', fg='white', font=self.font2)
        self.lb3.place(x=7, y=130)
        self.lb4 = Label(self, text='Data da compra:', bg='gray14', fg='white', font=self.font2)
        self.lb4.place(x=7, y=300)
        self.valor = Label(self, text='VALOR DE VENDA:', bg='gray14', fg='white', font=self.font)
        self.valor.place(x=7, y=193)
        # entrys
        self.ed1 = Entry(self, width=20)
        self.ed1.place(x=165, y=104)
        self.ed2 = Entry(self, width=23)
        self.ed2.place(x=146, y=133)
        self.ed3 = Entry(self, width=10)
        self.ed3.place(x=140, y=305)
        self.ed4 = Entry(self, width=15)
        self.ed4.place(x=225, y=200)
        # botao confirm
        self.bt = Button(self, width=10, height=3, bg='lime green', text='Continuar', command=self.mustangaba)
        self.bt.place(x=300, y=320)

    # -------------------
    def mustangaba(self):
        super().__init__()

        self.geometry("400x400+750+100")
        self.title("NOTA")
        self["bg"] = 'gray14'
        self.font = ('Verdana', '18', 'bold')
        self.font2 = ('Gotham', '16', 'italic')
        self.font3 = ('Verdana', '11')
        self.font4 = ('Verdana', '16', 'bold')
        self.font5 = ('Gotham', '16', 'bold')

        self.lb = Label(self, text='Compra efetuada!', bg='gray14', fg='white', font=self.font)
        self.lb.place(x=20, y=15)
        self.lb2 = Label(self, text='Mustang 2018               R$370.990 ', bg='gray14', fg='yellow2', font=self.font2)
        self.lb2.place(x=18, y=80)
        self.lb3 = Label(self, text='Comprador:', bg='gray14', fg='red2', font=self.font3)
        self.lb3.place(x=18, y=150)
        self.lb4 = Label(self, text='Vendedor:', bg='gray14', fg='red2', font=self.font3)
        self.lb4.place(x=18, y=190)
        self.lb5 = Label(self, text='Data de compra:', bg='gray14', fg='red2', font=self.font3)
        self.lb5.place(x=18, y=290)
        self.lb6 = Label(self, text='Valor:R$', bg='gray14', fg='white', font=self.font5)
        self.lb6.place(x=200, y=360)

        self.nomevendedor = Label(self, text=self.ed2.get(), bg='gray14', fg='white', font=self.font5)
        self.nomevendedor.place(x=115, y=150)
        self.nomecliente = Label(self, text=self.ed1.get(), bg='gray14', fg='white', font=self.font5)
        self.nomecliente.place(x=100, y=190)
        self.datacompra = Label(self, text=self.ed3.get(), bg='gray14', fg='white', font=self.font5)
        self.datacompra.place(x=150, y=290)
        self.valorvenda = Label(self, text=self.ed4.get(), bg='gray14', fg='yellow', font=self.font5)
        self.valorvenda.place(x=290, y=360)
#------------------------------------------------------------------------------------------------------------------
class Porsche(Toplevel):
    def __init__(self):
        super().__init__()
        self['bg'] = 'gray14'
        self.geometry('400x400+750+100')
        self.title('Detalhes da Compra')
        self.font = ('Verdana', '16', 'bold')
        self.font2 = ('Verdana', '11')

        self.lb = Label(self, text='DADOS FINAIS!', bg='gray14', fg='cyan2', font=self.font)
        self.lb.place(x=100, y=30)
        self.lb2 = Label(self, text='Nome do vendedor:', bg='gray14', fg='white', font=self.font2)
        self.lb2.place(x=7, y=100)
        self.lb3 = Label(self, text='Nome do Cliente:', bg='gray14', fg='white', font=self.font2)
        self.lb3.place(x=7, y=130)
        self.lb4 = Label(self, text='Data da compra:', bg='gray14', fg='white', font=self.font2)
        self.lb4.place(x=7, y=300)
        self.valor = Label(self, text='VALOR DE VENDA:', bg='gray14', fg='white', font=self.font)
        self.valor.place(x=7, y=193)
        # entrys
        self.ed1 = Entry(self, width=20)
        self.ed1.place(x=165, y=104)
        self.ed2 = Entry(self, width=23)
        self.ed2.place(x=146, y=133)
        self.ed3 = Entry(self, width=10)
        self.ed3.place(x=140, y=305)
        self.ed4 = Entry(self, width=15)
        self.ed4.place(x=225, y=200)
        # botao confirm
        self.bt = Button(self, width=10, height=3, bg='lime green', text='Continuar', command=self.porscheaba)
        self.bt.place(x=300, y=320)

    # -------------------
    def porscheaba(self):
        super().__init__()

        self.geometry("400x400+750+100")
        self.title("NOTA")
        self["bg"] = 'gray14'
        self.font = ('Verdana', '18', 'bold')
        self.font2 = ('Gotham', '16', 'italic')
        self.font3 = ('Verdana', '11')
        self.font4 = ('Verdana', '16', 'bold')
        self.font5 = ('Gotham', '16', 'bold')

        self.lb = Label(self, text='Compra efetuada!', bg='gray14', fg='white', font=self.font)
        self.lb.place(x=20, y=15)
        self.lb2 = Label(self, text='Porsche 2016               R$430.990 ', bg='gray14', fg='yellow2', font=self.font2)
        self.lb2.place(x=18, y=80)
        self.lb3 = Label(self, text='Comprador:', bg='gray14', fg='red2', font=self.font3)
        self.lb3.place(x=18, y=150)
        self.lb4 = Label(self, text='Vendedor:', bg='gray14', fg='red2', font=self.font3)
        self.lb4.place(x=18, y=190)
        self.lb5 = Label(self, text='Data de compra:', bg='gray14', fg='red2', font=self.font3)
        self.lb5.place(x=18, y=290)
        self.lb6 = Label(self, text='Valor:R$', bg='gray14', fg='white', font=self.font5)
        self.lb6.place(x=200, y=360)

        self.nomevendedor = Label(self, text=self.ed2.get(), bg='gray14', fg='white', font=self.font5)
        self.nomevendedor.place(x=115, y=150)
        self.nomecliente = Label(self, text=self.ed1.get(), bg='gray14', fg='white', font=self.font5)
        self.nomecliente.place(x=100, y=190)
        self.datacompra = Label(self, text=self.ed3.get(), bg='gray14', fg='white', font=self.font5)
        self.datacompra.place(x=150, y=290)
        self.valorvenda = Label(self, text=self.ed4.get(), bg='gray14', fg='yellow', font=self.font5)
        self.valorvenda.place(x=290, y=360)