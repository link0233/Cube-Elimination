from tkinter import*

from covor.covor import covor

class main(Canvas):
    def __init__(self):
        self.root=Tk()
        self.root.title('方塊消消樂')
        super(main,self).__init__(self.root,width=640,height=480)
        self.pack()
        self.covor=covor(self)
        self.root.mainloop()

if __name__=='__main__':
    main()