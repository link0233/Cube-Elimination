from covor.text import text
from covor.strat_button import start_button 

class covor:
    def __init__(self,canvas):
        self.cavnas=canvas
        self.cavnas.create_rectangle(0,0,640,480,fill='#000000')
        self.text=text(canvas)
        self.button=start_button(canvas)
    
    def loop(self):
        pass