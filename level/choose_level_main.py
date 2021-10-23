from level.choose_level import choose

class choose_level_main:
    def __init__(self,canvas):
        self.canvas=canvas
        self.choose=choose(canvas)
        self.text=''
        with open('./level/level.csv','r') as f:
            for i in f:
                self.text+=i
        self.text=self.text.split('\n')
        self.textt=[]
        for text in self.text:
            self.textt.append(text.split(','))
        self.text=[]
        for text in self.textt:
            self.text.append({
                'level':text[0],
                'score':text[1]
            })
        print(self.text)

    def choose_level_start(self):
        self.canvas.create_rectangle(0,0,640,480,fill='skyblue')
        self.xy=[0,37]
        self.t=0
        for text in self.text:
            self.t+=1   
            if self.t>10:
                self.t=0
                self.xy[0]=0
                self.xy[1]+=37
            self.xy[0]+=37
            self.choose.level_choose_start(text,self.xy)