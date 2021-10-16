class text:
    def __init__(self,canvas):
        self.canvas=canvas
        self.item=self.canvas.create_text(320,100,font=('Arial',50),fill='#ffffff',text='方塊消消樂')

    def delete(self):
        self.canvas.delete(self.item)