from level.choose_level import choose

class choose_level_main:
    def __init__(self,canvas):
        self.canvas=canvas
        self.choose=choose(canvas)

    def choose_level_start(self):
        self.canvas.create_rectangle(0,0,640,480,fill='skyblue')
        self.choose.level_choose_start({'level':1,'score':13},[100,100])