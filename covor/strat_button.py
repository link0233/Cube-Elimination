class start_button:
    def __init__(self,canvas):
        self.canvas=canvas
        self.btn={'bk':self.canvas.create_rectangle(220,200,420,240,fill='White')
                ,'text':self.canvas.create_text(320,220,text='繼續遊戲',font=('Arial',20),fill='#000000')
        }
        self.xy=[320,220]

    def loop(self,key):
        self.canvas.delete(self.btn['bk'])
        self.canvas.delete(self.btn['text'])
        if abs(key['xy'][0]-self.xy[0])<100 and abs(key['xy'][1]-self.xy[1])<20:
            self.btn={'bk':self.canvas.create_rectangle(220,200,420,240,fill='#3b3b3b')
                ,'text':self.canvas.create_text(320,220,text='繼續遊戲',font=('Arial',20),fill='#000000')
            } 
        else:
            self.btn={'bk':self.canvas.create_rectangle(220,200,420,240,fill='White')
                ,'text':self.canvas.create_text(320,220,text='繼續遊戲',font=('Arial',20),fill='#000000')
            }
        return 0