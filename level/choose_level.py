class choose:
    def __init__(self,canvas,PhotoImage):
        self.cavnas=canvas
        self.PhotoImage=PhotoImage
        self.items=[]
    
    def level_choose_start(self,level,xy):
        if level['score']>level['star'][2]:
            self.t=self.PhotoImage(file='./level/star_image/three.png')
        elif level['score']>level['star'][1]:
            self.t=self.PhotoImage(file='./level/star_image/two.png')
        elif level['score']>level['star'][0]:
            self.t=self.PhotoImage(file='./level/star_image/one.png')
        else:
            self.t=self.PhotoImage(file='./level/star_image/none.png')
        self.items.append({
            'bk':self.cavnas.create_rectangle(xy[0]-27,xy[1]-27,xy[0]+27,xy[1]+27,fill='#d69fd3'),
            'number':self.cavnas.create_text(xy[0],xy[1]-10,text=level['level'],font=('Arial',10),fill='White'),
            'star':self.cavnas.create_image(xy[0],xy[1]+17,image=self.t),
            'score':int(level['score']),
            'level':level    
            })