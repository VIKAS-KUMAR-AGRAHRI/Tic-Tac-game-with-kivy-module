from tkinter.messagebox import NO
import kivy
from  kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class Mydesign(GridLayout):
    def __init__(self, **kwargs):
        self.count=1
        super(Mydesign,self).__init__(**kwargs)
        #Popup box main layout.............
        popbox=GridLayout(cols=1,rows=2)
        #popup label ...
        self.pl=Label(text='winner is',size_hint=(.5,.5))
        self.pb=Button(text='ok',size_hint=(.75,.75))
        popbox.add_widget(self.pl)
        popbox.add_widget(self.pb)
        #Popup creation....................
        print(self.width)
        print(self.height)
        self.pop=Popup(title='winner show', content=popbox,auto_dismiss=False,size_hint=(None,None),size=(self.width+70,self.height+80))

        #add dismiss button in 'ok' button...........................
        self.pb.bind(on_press=self.pop.dismiss)
        self.pb.bind(on_press=self.buttonreset)
        #popup creation end here....................
    def printfun(self,j):
        symbol=['X','O']
        red = [1, 0, 0, .7] 
        green = [0, 1, 0,.7]
        self.player1='Green'
        self.player2='Red'
        if(self.ids.one==j):
            if self.count%2!=0:
                self.ids.one.text=str(symbol[1])
                self.ids.one.disabled=True
                self.ids.one.background_color=red
            else:
                self.ids.one.text=str(symbol[0])
                self.ids.one.disabled=True
                self.ids.one.background_color=green
            print('one')
        elif(self.ids.two==j):
            if self.count%2!=0:
                self.ids.two.text=str(symbol[1])
                self.ids.two.disabled=True
                self.ids.two.background_color=red
            else:
                self.ids.two.disabled=True
                self.ids.two.background_color=green
                self.ids.two.text=str(symbol[0])
            print('two')
        elif(self.ids.three==j):
            if self.count%2!=0:
                self.ids.three.disabled=True
                self.ids.three.text=str(symbol[1])
                self.ids.three.background_color=red
            else:
                self.ids.three.disabled=True
                self.ids.three.text=str(symbol[0])
                self.ids.three.background_color=green
            print('three')
        elif(self.ids.four==j):
            if self.count%2!=0:
                self.ids.four.text=str(symbol[1])
                self.ids.four.disabled=True
                self.ids.four.background_color=red
            else:
                self.ids.four.disabled=True
                self.ids.four.text=str(symbol[0])
                self.ids.four.background_color=green
            print('four')
        elif(self.ids.five==j):
            if self.count%2!=0:
                self.ids.five.disabled=True
                self.ids.five.background_color=red
                self.ids.five.text=str(symbol[1])
            else:
                self.ids.five.disabled=True
                self.ids.five.text=str(symbol[0])
                self.ids.five.background_color=green
            print('five')
        elif(self.ids.six==j):
            if self.count%2!=0:
                self.ids.six.disabled=True
                self.ids.six.background_color=red
                self.ids.six.text=str(symbol[1])
            else:
                self.ids.six.disabled=True
                self.ids.six.text=str(symbol[0])
                self.ids.six.background_color=green
            print('six')
        elif(self.ids.seven==j):
            if self.count%2!=0:
                self.ids.seven.disabled=True
                self.ids.seven.text=str(symbol[1])
                self.ids.seven.background_color=red
            else:
                self.ids.seven.disabled=True
                self.ids.seven.text=str(symbol[0])
                self.ids.seven.background_color=green
            print('seven')
        elif(self.ids.eight==j):
            if self.count%2!=0:
                self.ids.eight.disabled=True
                self.ids.eight.background_color=red
                self.ids.eight.text=str(symbol[1])
            else:
                self.ids.eight.disabled=True
                self.ids.eight.text=str(symbol[0])
                self.ids.eight.background_color=green
            print('eight')
        elif(self.ids.nine==j):
            if self.count%2!=0:
                self.ids.nine.disabled=True
                self.ids.nine.background_color=red
                self.ids.nine.text=str(symbol[1])
            else:
                self.ids.nine.disabled=True
                self.ids.nine.background_color=green
                self.ids.nine.text=str(symbol[0])
            print('nine')
        if(self.count>=5):
            self.conditioncheck()
        self.count=self.count+1
        print('count',self.count)
    def conditioncheck(self):
        if ((self.ids.one.text=='X' and self.ids.two.text=='X' and self.ids.three.text=='X') or (self.ids.one.text=='O' and self.ids.two.text=='O' and self.ids.three.text=='O')):
            if(self.ids.one.text=='X'):
                print('Won X player')
                self.pl.text+=self.player1
                self.pop.open()
            else:
                print('Wor O Player')
                self.pl.text+=self.player2
                self.pop.open()
        elif ((self.ids.one.text=='X' and self.ids.four.text=='X' and self.ids.seven.text=='X') or (self.ids.one.text=='O' and self.ids.four.text=='O' and self.ids.seven.text=='O')):
            if(self.ids.one.text=='X'):
                print('Won X player')
                self.pl.text+=self.player1
                self.pop.open()
            else:
                print('Wor O Player')
                self.pl.text+=self.player2
                self.pop.open()
        elif ((self.ids.one.text=='X' and self.ids.five.text=='X' and self.ids.nine.text=='X') or (self.ids.one.text=='O' and self.ids.five.text=='O' and self.ids.nine.text=='O')):
            if(self.ids.one.text=='X'):
                print('Won X player')
                self.pl.text+=self.player1
                self.pop.open()
            else:
                print('Wor O Player')
                self.pl.text+=self.player2
                self.pop.open()
        elif ((self.ids.two.text=='X' and self.ids.five.text=='X' and self.ids.eight.text=='X') or (self.ids.two.text=='O' and self.ids.five.text=='O' and self.ids.eight.text=='O')):
            if(self.ids.two.text=='X'):
                print('Won X player')
                self.pl.text+=self.player1
                self.pop.open()
            else:
                print('Wor O Player')
                self.pl.text+=self.player2
                self.pop.open()
        elif ((self.ids.three.text=='X' and self.ids.six.text=='X' and self.ids.nine.text=='X') or (self.ids.three.text=='O' and self.ids.six.text=='O' and self.ids.nine.text=='O')):
            if(self.ids.three.text=='X'):
                print('Won X player')
                self.pl.text+=self.player1
                self.pop.open()
            else:
                print('Wor O Player')
                self.pl.text+=self.player2
                self.pop.open()
        elif ((self.ids.four.text=='X' and self.ids.five.text=='X' and self.ids.six.text=='X') or (self.ids.four.text=='O' and self.ids.five.text=='O' and self.ids.six.text=='O')):
            if(self.ids.four.text=='X'):
                print('Won X player')
                self.pl.text+=self.player1
                self.pop.open()
            else:
                print('Wor O Player')
                self.pl.text+=self.player2
                self.pop.open()
        elif ((self.ids.seven.text=='X' and self.ids.eight.text=='X' and self.ids.nine.text=='X') or (self.ids.seven.text=='O' and self.ids.eight.text=='O' and self.ids.nine.text=='O')):
            if(self.ids.seven.text=='X'):
                print('Won X player')
                self.pl.text+=self.player1
                self.pop.open()
            else:
                print('Wor O Player')
                self.pl.text+=self.player2
                self.pop.open()
        elif ((self.ids.three.text=='X' and self.ids.five.text=='X' and self.ids.seven.text=='X') or (self.ids.three.text=='O' and self.ids.five.text=='O' and self.ids.seven.text=='O')):
            if(self.ids.three.text=='X'):
                print('Won X player')
                self.pl.text+=self.player1
                self.pop.open()
            else:
                print('Wor O Player')
                self.pl.text+=self.player2
                self.pop.open()
        elif(self.count>=9):
            self.pl.text='Match Draw'
            self.pop.open()
    def buttonreset(self,event):
        self.pl.text='Winner is'
        self.count=1
        self.ids.one.text=''
        #color reset.....................
        self.ids.one.background_color=(.3,.3, 1, 1)
        self.ids.two.background_color=(.3,.3, 1, 1)
        self.ids.three.background_color=(.3,.3, 1, 1)
        self.ids.four.background_color=(.3,.3, 1, 1)
        self.ids.five.background_color=(.3,.3, 1, 1)
        self.ids.six.background_color=(.3,.3, 1, 1)
        self.ids.seven.background_color=(.3,.3, 1, 1)
        self.ids.eight.background_color=(.3,.3, 1, 1)
        self.ids.nine.background_color=(.3,.3, 1, 1)
        #color reset end....................
        self.ids.one.disabled=False
        self.ids.two.text=''
        self.ids.two.disabled=False
        self.ids.three.text=''
        self.ids.three.disabled=False
        self.ids.four.text=''
        self.ids.four.disabled=False
        self.ids.five.text=''
        self.ids.five.disabled=False
        self.ids.six.text=''
        self.ids.six.disabled=False
        self.ids.seven.text=''
        self.ids.seven.disabled=False
        self.ids.eight.text=''
        self.ids.eight.disabled=False
        self.ids.nine.text=''
        self.ids.nine.disabled=False
        

class MainApp(App):
    def build(self):
        return Mydesign()
if __name__=='__main__':
    MainApp().run()