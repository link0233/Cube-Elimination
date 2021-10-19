from tkinter import*
from time import sleep

from covor.covor import covor
from key import key

class main(Canvas):
    def __init__(self):
        self.root=Tk()
        self.root.title('方塊消消樂')
        super(main,self).__init__(self.root,width=640,height=480)
        self.pack()
        
        self.covor=covor(self)
        self.key=key(self)

        self.covort()
        self.load()

        self.root.mainloop()

    def covort(self):
        self.f=0
        while self.f==0:
            self.f=self.covor.loop(self.key.key)
            self.update()

    def load(self):
        self.window=self.create_rectangle(640,0,1280,480,fill='#54aec9')
        for i in range(64):
            self.move(self.window,-10,0)
            self.update()
        self.covor.delete()
        self.delete(self.window)

        self.window=self.create_rectangle(0,0,640,480,fill='#54aec9')
        for i in range(64):
            self.move(self.window,-10,0)
            self.update()
        self.delete(self.window)

    def update(self):
        self.key.loop()
        self.root.update()
        sleep(0.01)

if __name__=='__main__':
    main()