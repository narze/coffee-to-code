import tkinter as tk
import random
import math
import time
import threading

globalBoard = []
codeArr = []

def main():
    global globalBoard
    root = tk.Tk()
    root.title("Click to add cell, Right click to remove, help the program convert code to coffee or hinder it")
    myCanvas, globalBoard = setUp(root,500,500)
    generateDefaultBoardState(myCanvas,globalBoard)
    root.mainloop()

def generateDefaultBoardState(canvas,board):
    global codeArr
    x = 0
    y = 0
    for row in board:
        y=0
        for cell in row:
            drawSquare(x,y,canvas,board,False)
            y+=1
        x+=1
    u = 10
    c = drawLine(10,13,"x",20,canvas,False) + drawLine(21,25,"y",10,canvas,False) + drawLine(10,13,"x",25,canvas,False)
    o = drawLine(15,19,"x",20,canvas,False) + drawLine(15,19,"x",25,canvas,False) + drawLine(20,25,"y",19,canvas,False) + drawLine(20,25,"y",15,canvas,False)
    d = drawLine(20,25,"y",21,canvas,False) + drawLine(21,24,"x",25,canvas,False) + drawLine(21,24,"x",20,canvas,False) +drawLine(21,24,"y",25,canvas,False)
    e = drawLine(27,30,"x",20,canvas,False) + drawLine(27,30,"x",23,canvas,False) + drawLine(27,30,"x",25,canvas,False) + drawLine(20,25,"y",27,canvas,False)
    codeArr = c+o+d+e
    #C
    drawLine(5,8,"x",20,canvas)
    drawLine(21,25,"y",5,canvas)
    drawLine(5,8,"x",25,canvas)
    #O
    drawLine(10,14,"x",20,canvas)
    drawLine(10,14,"x",25,canvas)
    drawLine(20,25,"y",14,canvas)
    drawLine(20,25,"y",10,canvas)
    #F
    drawLine(17,19,"x",20,canvas)
    drawLine(17,19,"x",22,canvas)
    drawLine(20,25,"y",16,canvas)
    #F
    drawLine(21,24,"x",20,canvas)
    drawLine(21,24,"x",22,canvas)
    drawLine(20,25,"y",21,canvas)
    #E
    drawLine(26,29,"x",20,canvas)
    drawLine(26,29,"x",23,canvas)
    drawLine(26,29,"x",25,canvas)
    drawLine(20,25,"y",26,canvas)
    #E
    drawLine(31,34,"x",20,canvas)
    drawLine(31,34,"x",23,canvas)
    drawLine(31,34,"x",25,canvas)
    drawLine(20,25,"y",31,canvas)
    
def clickEvent(event,canvas,tf):
    global globalBoard
    x = event.x//10
    y = event.y//10
    drawSquare(x,y,canvas,globalBoard,tf)
    
def drawLine(pos1,pos2,xy,pos3,canvas,tf=True):
    global globalBoard
    if(xy =="x" and tf==True):
        i=0
        for i in range(abs(pos1-pos2-1)):
            drawSquare(pos1+i,pos3,canvas,globalBoard,True)
            i+=1
    elif(xy =="y"and tf==True):
        for i in range(abs(pos1-pos2-1)):
            drawSquare(pos3,pos1+i,canvas,globalBoard,True)
            i+=1
    elif(xy=="x"):
        arr = []
        for i in range(abs(pos1-pos2-1)):
            arr.append({"x":pos1+i,"y":pos3})
            i+=1
        return arr
    elif(xy=="y"):
        arr = []
        for i in range(abs(pos1-pos2-1)):
            arr.append({"x":pos3,"y":pos1+i})
            i+=1
        return arr
def tick(canvas):
    global globalBoard
    global codeArr
    for row in globalBoard:
        
        for cell in row:
                if(cell["val"]==1):
                    shouldContinue = False
                    for value in codeArr:
                        if(value["x"] == cell["x"] and value["y"] == cell["y"] and globalBoard[cell["x"]][cell["y"]]["val"]==1):
                            print(f"cell x: " + str(cell["x"]) + "cell y: " +str(cell["y"]))
                            shouldContinue = True
                            break    
                    if(shouldContinue ==True):
                        continue
                    drawSquare(cell["x"],cell["y"],canvas,globalBoard,False)
                    rand = math.floor(random.uniform(-1, 2.5))
                    rand2 = math.floor(random.uniform(-1, 2.5))
                    if(cell["x"]+rand > len(globalBoard)-2 or cell["x"]+rand > len(globalBoard[1])-2 or cell["x"] < 0):
                        drawSquare(math.floor(random.uniform(0, 20)),math.floor(random.uniform(0, 20)),canvas,globalBoard,True)
                        return globalBoard
                    if(cell["y"]+rand2 > len(globalBoard)-2 or cell["y"]+rand2 > len(globalBoard[1])-2 or cell["y"] < 0):
                        drawSquare(math.ceil(random.uniform(0, 20)),math.ceil(random.uniform(0, 20)),canvas,globalBoard,True)
                        return globalBoard
                    
                    drawSquare(cell["x"]+rand,cell["y"]+rand2,canvas,globalBoard,True)
    drawSquare(math.ceil(random.uniform(0, 48)),math.ceil(random.uniform(0, 48)),canvas,globalBoard,True)
    drawSquare(math.ceil(random.uniform(0, 48)),math.ceil(random.uniform(0, 48)),canvas,globalBoard,True)
    return globalBoard
            
def drawSquare(posx,posy,canvas,board,live):
    if(live == True):
        board[posx][posy] = {"val":1,"x":posx,"y":posy}
        posx = posx*10
        posy =posy*10
        canvas.create_rectangle(0+posx,0+posy,10+posx,10+posy,fill="#000000",outline="#a8a8a8")
    else:
        board[posx][posy] = {"val":0,"x":posx,"y":posy}
        posx = posx*10
        posy =posy*10
        canvas.create_rectangle(0+posx,0+posy,10+posx,10+posy,fill="#ffffff",outline="#e6e6e6")
    return

def setUp(root,x,y):
    myCanvas = tk.Canvas(root, bg="white", height=y, width=y)
    def lClick(event,canvas=myCanvas):
        return clickEvent(event,canvas,True)
    def rClick(event,canvas=myCanvas):
        return clickEvent(event,canvas,False)
    myCanvas.bind("<Button-1>",lClick)
    myCanvas.bind("<Button-3>",rClick)
    board = []
    for i in range(int(y//10)):
        line = []
        z=0
        for z in range(int(x//10)):
            line.append(0)
            z+=1
        board.append(line)
        i+=1
    myCanvas.pack()
    btnFrame = tk.Frame(root)
    btnFrame.pack(side="bottom")
    startBtn = tk.Button(btnFrame,text="Start",bg='#dbdbdb')
    startBtn.config(command=lambda: toggle(myCanvas,startBtn))
    editBtn = tk.Button(btnFrame,text="Reset",bg='#dbdbdb')
    editBtn.config(command=lambda: clear(myCanvas,editBtn))
    startBtn.pack(side="left")
    editBtn.pack(side="left")
    return myCanvas, board

def toggle(canvas,btn):
    changeBtnColorOnPress(btn,'#02eb40',"Start","Stop")
    if(btn["bg"] == '#02eb40'):
        def subTick():
            while(btn["bg"] == '#02eb40'):
                global globalBoard
                globalBoard = tick(canvas)
                time.sleep(.1)
        x = threading.Thread(target=subTick)
        x.start()
        
def clear(canvas,btn):
    global globalBoard
    #changeBtnColorOnPress(btn,'#858585',"edit","stop editing")
    generateDefaultBoardState(canvas,globalBoard)
    
def changeBtnColorOnPress(btn,color,text1,text2,defaultColor='#dbdbdb'):
    if(btn["bg"]==color):
        btn.config(bg=defaultColor,text=text1)
    else:
        btn.config(bg=color,text=text2)
if __name__ == '__main__':
    main()