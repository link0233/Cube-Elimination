from covor.text import text

class covor:
    def __init__(self,canvas):
        self.cavnas=canvas
        self.cavnas.create_rectangle(0,0,640,480,fill='#000000')
        self.text=text(canvas)