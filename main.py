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

        self.root.mainloop()

    def covort(self):
        self.f=0
        while self.f==0:
            self.covor.loop()
            self.update()

    def update(self):
        self.key.loop()
        self.root.update()
        sleep(0.01)

if __name__=='__main__':
    main()