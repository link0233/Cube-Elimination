from covor.text import text
from covor.strat_button import start_button 

class covor:
    def __init__(self,canvas):
        self.cavnas=canvas
        self.item=self.cavnas.create_rectangle(0,0,640,480,fill='#000000')
        self.text=text(canvas)
        self.button=start_button(canvas)
    
    def loop(self,key):
        return self.button.loop(key)

    def delete(self):
        self.text.delete()
        self.button.delete()
        self.cavnas.delete(self.item)