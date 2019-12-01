from tkinter import Tk as makescreen, Canvas, PhotoImage

screen = makescreen()
screen.title('Center View Game')
screen.resizable(0,0)
screen.wm_attributes("-topmost", 1)

canvas = Canvas(screen, width = 600, height = 600)
canvas.pack()
screen.update()

bgimage = PhotoImage(file = 'background.png')
walk0image = PhotoImage(file = 'walk0.png')
walk1image = PhotoImage(file = 'walk1.png')
walk2image = PhotoImage(file = 'walk2.png')
walk3image = PhotoImage(file = 'walk3.png')
walk4image = PhotoImage(file = 'walk4.png')
standimage = PhotoImage(file = 'stand.png')
tree0image = PhotoImage(file = 'tree0.png')
tree1image = PhotoImage(file = 'tree1.png')
flower0image = PhotoImage(file = 'flower0.png')
flower1image = PhotoImage(file = 'flower1.png')
boy0image = PhotoImage(file = 'boy0.png')
boy1image = PhotoImage(file = 'boy1.png')

canvas.create_image(300, 300, image = bgimage)
walklist = [ walk0image, walk1image, walk2image, walk3image, walk4image, walk3image, walk2image, walk1image ]
girl = canvas.create_image(300, 330, image = walk0image)
index = 0

iswalk = False
def walk() :
    global index
    if iswalk == True :
            index += 1
            canvas.itemconfig(girl, image = walklist[index%8])
    else :
            canvas.itemconfig(girl, image = standimage)
    canvas.after(200, walk)
walk()


def left(event) :
    global iswalk
    iswalk = True

def stop(event) :
    global iswalk
    iswalk = False

canvas.bind_all("<KeyPress-Left>", left)
canvas.bind_all("<KeyRelease-Left>", stop)
    
screen.mainloop()
