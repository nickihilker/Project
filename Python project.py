from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='black')
player = drawpad.create_rectangle(400,595,405,600, fill="green")
enemy1 = drawpad.create_rectangle(50,50,100,60, fill="red")
enemy2 = drawpad.create_rectangle(250,250,300,260, fill="red")
enemy3 = drawpad.create_rectangle(450,450,500,460, fill="red")
dead = False
drawpadwidth = 800
drawpadheight = 600
direction1 = 5
direction2 = -7
direction3 = 9
class myApp(object):
    def __init__(self, parent):
        global drawpad
        self.myParent = parent
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
# Enter my text
        self.prompt = "Lives left :"
        self.label1 = Label(root, text=self.prompt, width=len(self.prompt), bg='green')
        self.label1.pack()
        
        self.lives = 5
        self.livesTxt = Label(root, text=str(self.lives), width=len(str(self.lives)), bg='green')
        self.livesTxt.pack()
        self.dead = False
# Adding the drawpad, adding the key listener, starting animation
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
    def animate(self):
        global drawpad
        global enemy1
        global enemy2
        global enemy3
        global direction1
        global direction2
        global direction3
        global player
        x1,y1,x2,y2 = drawpad.coords(enemy1)
        ex1,ey1,ex2,ey2 = drawpad.coords(enemy2)
        tx1,ty1,tx2,ty2 = drawpad.coords(enemy3)
        px1,py1,px2,py2 = drawpad.coords(player)
    
        if x2 > 800:
            direction1 = - 5
        elif x1 < 0:
            direction1 = 5
        if ex2 > 800:
            direction2 = - 5
        elif ex1 < 0:
            direction2 = 5
        if tx2 > 800:
            direction3 = - 5
        elif tx1 < 0:
            direction3 = 5
        drawpad.move(enemy1, direction1, 0)
        
        drawpad.move(enemy2, direction2, 0)
        drawpad.move(enemy3, direction3, 0)
        drawpad.after(5,self.animate)
        didWeHit = self.collisionDetect()
        if didWeHit == False:
            drawpad.after(1,self.animate)
        if self.lives > 0:
            self.dead = True
            self.lives = self.lives - 1
            self.livesTxt.configure(text=self.lives)
    def key(self,event):
        global player
        global drawpadheight
        global drawpadwidth
        px1, py1, px2, py2 = drawpad.coords(player)
        if event.char == "w":
            if (py1 > 0):
                drawpad.move(player,0,-4)
#Added ASD movement and boundary detection
        if event.char == "s":
            if (py2 < 600):
                drawpad.move(player,0,4)
        if event.char == "a":
            if (px1 > 0):
                drawpad.move(player,-4,0)
        if event.char == "d":
            if (px2 < 800):
                drawpad.move(player,4,0)
# Makes the rocket fire, return, and count down the text
    def collisionDetect(self):
        global enemy1
        global enemy2
        global enemy3
        global drawpad
        global player
        px1,py1,px2,py2 = drawpad.coords(player)
        x1,y1,x2,y2 = drawpad.coords(enemy1)
        ex1,ey1,ex2,ey2 = drawpad.coords(enemy2)
        tx1,ty1,tx2,ty2 = drawpad.coords(enemy3)
        if (px1 > tx1 and px2 < tx2) and (py1 > ty1 and py2 < ty2):
            return True
        elif (px1 > x1 and px2 < x2) and (py1 > y1 and py2 < y2):
            return True
        elif (px1 > ex1 and px2 < ex2) and (py1 > ey1 and py2 < ey2):
            return True
        else:
            return False
app = myApp(root)
root.mainloop()