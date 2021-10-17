class key:
    def __init__(self,canvas):
        self.key={
            'xy':[0,0],
            'button1':0
        }
        canvas.bind('<Motion>',self.mot)
        canvas.bind('<Button-1>',self.but1)
        
    def loop(self):
        self.key['button1']=0

    def mot(self,event):
        self.key['xy']=[event.x,event.y]

    def but1(self,event):
        self.key['button1']=1