from tkinter import *


class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.color = "black"
        self.brush_size = 2
        self.setUI()

    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self, new_size):
        self.brush_size = new_size

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)

    def setUI(self):

        self.parent.title("Paint")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(6, weight=1)
        self.rowconfigure(2, weight=1)

        self.canv = Canvas(self, bg="white")
        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5, sticky=E+W+S+N)
        self.canv.bind("<B1-Motion>", self.draw)

        color_lab = Label(self, text="Color: ")
        color_lab.grid(row=0, column=0, padx=6)

        red_btn = Button(self, text="Red", width=10,
                         command=lambda: self.set_color("red"))
        red_btn.grid(row=0, column=1)
        orange_btn = Button(self, text="Orange", width=10,
                        command=lambda: self.set_color("orange"))
        orange_btn.grid(row=0, column=2)
        blue_btn = Button(self, text="Blue", width=10,
                          command=lambda: self.set_color("blue"))
        blue_btn.grid(row=0, column=3)
        yellow_btn = Button(self, text="Yellow", width=10,
                           command=lambda: self.set_color("yellow"))
        yellow_btn.grid(row=0, column=4)
        pink_btn = Button(self, text="Pink", width=10,
                           command=lambda: self.set_color("pink"))
        pink_btn.grid(row=0, column=5)

        clear_btn = Button(self, text="Clear all", width=10,
                           command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=1, column=6, sticky=W)

        size_lab = Label(self, text="Brush size: ")
        size_lab.grid(row=1, column=0, padx=5)
        one_btn = Button(self, text="Two", width=10,
                         command=lambda: self.set_brush_size(2))
        one_btn.grid(row=1, column=1)
        two_btn = Button(self, text="Three", width=10,
                         command=lambda: self.set_brush_size(3))
        two_btn.grid(row=1, column=2)
        third_btn = Button(self, text="Four", width=10,
                         command=lambda: self.set_brush_size(4))
        third_btn.grid(row=1, column=3)
        four_btn = Button(self, text="Five", width=10,
                         command=lambda: self.set_brush_size(5))
        four_btn.grid(row=1, column=4)
        five_btn = Button(self, text="Ten", width=10,
                         command=lambda: self.set_brush_size(10))
        five_btn.grid(row=1, column=5)

def main():
    root = Tk()
    root.geometry("600x500+300+300")
    app = Paint(root)
    root.mainloop()
if __name__ == '__main__':
    main()
