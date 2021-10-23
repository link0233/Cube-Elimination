class choose:
    def __init__(self,canvas):
        self.cavnas=canvas
        self.items=[]
    
    def level_choose_start(self,level,xy):
        self.items.append({
            'bk':self.cavnas.create_rectangle(xy[0]-27,xy[1]-27,xy[0]+27,xy[1]+27,fill='#d69fd3'),
            'number':self.cavnas.create_text(xy[0],xy[1],text=str(level['level']),font=('Arial',15),fill='White'),
            'score':level['score'],
            'level':level    
            })