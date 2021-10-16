from tkinter import*

class main(Canvas):
    def __init__(self):
        self.root=Tk()
        self.root.title('方塊消消樂')
        super(main,self).__init__(self.root,width=640,height=480)
        self.pack()
        self.root.mainloop()

if __name__=='__main__':
    main()