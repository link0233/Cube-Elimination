class start_button:
    def __init__(self,canvas):
        self.canvas=canvas
        self.btn={'bk':self.canvas.create_rectangle(220,200,420,240,fill='White')
                ,'text':self.canvas.create_text(320,220,text='繼續遊戲',font=('Arial',20),fill='#000000')
        }