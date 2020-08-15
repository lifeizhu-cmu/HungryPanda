from cmu_112_graphics import *
from tkinter import *
from PIL import Image
import random
import math
class Panda(object):
    def __init__(self,sprite,x,y):
        self.frame = 0
        self.sprite = sprite
        self.x = x
        self.y = y
        self.pandaWidth = 89
        self.pandaHeight = 75
    def panda_timerFired(self):
        self.frame += 1
        self.frame %= len(self.sprite)
    def panda_redrawAll(self,canvas,cx,cy):
        frameNew = self.sprite[self.frame]
        canvas.create_image(cx, cy, image=ImageTk.PhotoImage(frameNew))

class NewPanda(object):
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.newPandaWidth = 45
        self.newPandaHeight = 45
        self.newPandaImage = img
    def panda_redrawAll(self,canvas,cx,cy):
        canvas.create_image(cx, cy, image=ImageTk.PhotoImage(self.newPandaImage))
class Brick(object):
    def __init__(self,col,row):
        self.col = col
        self.row = row
        self.dx = 10
        self.size = 20
        self.x = 20 + col * 20
        self.y = 20 + row * 20
        print(self.x,self.y)
    def brick_timerFired(self):
        self.x+=self.dx
        if self.x<20 or self.x+2*self.size>500:
            self.x-=self.dx
            self.dx=-self.dx       
    def brick_redrawAll(self,canvas):
        canvas.create_rectangle(self.x,self.y,self.x+self.size,self.y+self.size,
                                fill='yellow')
class Wood(object):
    def __init__(self,col,row,img):
        self.col = col
        self.row = row
        self.dx = 10
        self.size = 20
        self.x = 20 + col * 20
        self.y = 20 + row * 20
        print(self.x,self.y)
        self.img = img
    def wood_timerFired(self):
        if self.row%2==0:
            self.x+=self.dx
            if self.x>500:
                self.x=20
        else:
            self.x-=self.dx
            if self.x<20:
                self.x=500
    def wood_redrawAll(self,canvas):
        canvas.create_image(self.x,self.y, 
                            image=ImageTk.PhotoImage(self.img))
class Fire(object):
    def __init__(self,sprite,x,y):
        self.frame = 0
        self.sprite = sprite
        self.x = x
        self.y = y
        self.fireWidth = 48
        self.fireHeight = 48
    def __hash__(self):
        return hash(mode.sprite)
    def __eq__(self,other):
        return isinstance(other,Fire) and other.x==self.x and other.y==self.y    
    def fire_timerFired(self):
        self.frame += 1
        self.frame %= len(self.sprite)
    def fire_redrawAll(self,canvas,cx,cy):
        frameNew = self.sprite[self.frame]
        canvas.create_image(cx, cy, image=ImageTk.PhotoImage(frameNew))       
class SplashScreenMode(Mode):
    def appStarted(mode):
        urlStart = 'https://i.loli.net/2019/11/21/j5ty7kFMuGo4iUH.png'
        spriteStart = mode.loadImage(urlStart)
        spriteOutStart = mode.scaleImage(spriteStart,1.3)
        mode.screenStart = spriteOutStart
        urlClosedBox = 'https://i.loli.net/2019/11/24/Wo2uBZxpygFQvGH.png'
        spritestripClosedBox0 = mode.loadImage(urlClosedBox)
        spritestripClosedBox = mode.scaleImage(spritestripClosedBox0, 1/5)
        mode.closedBox = spritestripClosedBox
        urlOpenBox = 'https://i.loli.net/2019/11/21/gH2Q6fNZbMjeqCv.png'
        spritestripOpenBox0 = mode.loadImage(urlOpenBox)
        spritestripOpenBox = mode.scaleImage(spritestripOpenBox0, 1/10)
        mode.OpenBox = spritestripOpenBox
        mode.cursorImage = mode.closedBox      
        mode.cursor = (0,0)
        urlQuestion = 'https://i.loli.net/2019/11/24/5AHx69UwigonXQj.png'
        spritestripurlQuestion0 = mode.loadImage(urlQuestion)
        spritestripurlQuestion = mode.scaleImage(spritestripurlQuestion0, 1/15)
        mode.question = spritestripurlQuestion
    def mouseMoved(mode,event):
        mode.cursor = (event.x,event.y)
        if 20<=event.x<=120  and  mode.height-90<=event.y<=mode.height-10 :
            mode.cursorImage = mode.OpenBox
        elif (mode.width-120<=event.x<=mode.width-20  and 
                mode.height-90<=event.y<=mode.height-10) :
            mode.cursorImage = mode.question
        else:
            mode.cursorImage = mode.closedBox

    def mousePressed(mode,event):
        mode.cursor = (event.x,event.y)
        if 20<=event.x<=mode.width-120  and  mode.height-90<=event.y<=mode.height-10 :
            mode.app.setActiveMode(mode.app.mapModeOne)
        elif (mode.width-120<=event.x<=mode.width-20  and 
              mode.height-90<=event.y<=mode.height-10) :
            mode.app.setActiveMode(mode.app.helpModeOne)        

    def redrawAll(mode, canvas):
        canvas.create_image(mode.width//2,mode.height//2, 
                            image=ImageTk.PhotoImage(mode.screenStart))
        font = 'Arial 26 bold'
        canvas.create_text(mode.width/2, 50, text='Welcome to Hungry Panda!', font=font)
        canvas.create_text(mode.width/2, 150, 
        text='Help the panda to win the bamboo', font=font)
        canvas.create_text(mode.width/2, 250, 
        text='THREE steps to win', font=font)
        canvas.create_text(mode.width/2, 350, 
        text='Click START to take this adventure',fill='red', font=font)
        canvas.create_text(mode.width/2, 450, text='Click HELP for help!', font=font)
        canvas.create_rectangle(20,mode.height-90,120,mode.height-10,fill='yellow')
        canvas.create_text(70, mode.height-50, text='START', font=font)
        canvas.create_rectangle(mode.width-120,mode.height-90,
                                mode.width-20,mode.height-10,fill='yellow')
        canvas.create_text(mode.width-70, mode.height-50, text='HELP', font=font)
        curX,curY = mode.cursor
        canvas.create_image(curX,curY, image=ImageTk.PhotoImage(mode.cursorImage))

    def keyPressed(mode, event):
        mode.app.setActiveMode(mode.app.gameModeThree)
class GameModeOne(Mode):
    def appStarted(mode):
        urlBackground = 'https://i.loli.net/2019/12/03/BMIPVSbm1kEvWOj.png'
        spritestripBg0 = mode.loadImage(urlBackground)
        spritestripBg = mode.scaleImage(spritestripBg0, 1/6)
        mode.bgImage = spritestripBg
        urlBackgroundTwo = 'https://i.loli.net/2019/12/05/ng8FYm72Jeowr9W.png'
        spritestripBgTwo0 = mode.loadImage(urlBackgroundTwo)
        spritestripBgTwo = mode.scaleImage(spritestripBgTwo0, 0.45)
        mode.bgImageTwo = spritestripBgTwo
        urlCliff = 'https://i.loli.net/2019/12/05/CKIgPsVxuHEwepd.png'
        spritestripCliff0 = mode.loadImage(urlCliff)
        spritestripCliff = mode.scaleImage(spritestripCliff0, 0.6)
        mode.cliffImage = spritestripCliff
        urlEmpty = 'https://i.loli.net/2019/12/05/FsnOwpIG5P9Ty6f.png'
        spritestripEmpty0 = mode.loadImage(urlEmpty)
        spritestripEmpty = mode.scaleImage(spritestripEmpty0, 1/8)
        mode.emptyImage = spritestripEmpty    
        url = 'https://i.loli.net/2019/11/24/9qpgztci7MUSLBP.png'
        spritestrip0 = mode.loadImage(url)
        spritestrip = mode.scaleImage(spritestrip0, 0.5)
        mode.spritesRight = []
        for i in range(9):
            sprite = spritestrip.crop((89*i, 0, 89*(i+1), 75))
            mode.spritesRight.append(sprite)
        mode.pandaX = 45 # panda's center
        mode.pandaY = mode.height//3-35 # panda's center
        mode.panda = Panda(mode.spritesRight,mode.pandaX,mode.pandaY)
        urlOpenBox = 'https://i.loli.net/2019/11/24/fHiR7lzkC2yvcbN.png'
        spritestripOpenBox0 = mode.loadImage(urlOpenBox)
        spritestripOpenBox = mode.scaleImage(spritestripOpenBox0, 1/8)
        mode.cursorImage = spritestripOpenBox
        mode.emptyImageCopy = spritestripOpenBox
        mode.cursor = (mode.width//5+50,0)
        mode.dy=0
        mode.dx=2
        mode.up=False
        mode.isPaused=False
        mode.scrollX=0
        mode.scrollMarginX=mode.width/2.5
    def checkBoundary(mode):
        if (mode.width//5<mode.panda.x<4*mode.width//5 or \
            6*mode.width//5<mode.panda.x<9*mode.width//5 ):
            mode.panda.x+=mode.dx
            mode.panda.y+=mode.dy
            mode.dy+=3
            if mode.panda.y>2*mode.height//3 :
                if mode.width//5<mode.panda.x<4*mode.width//5:
                    if mode.cursor[0]-80<mode.panda.x<mode.cursor[0]+80:
                        mode.dy*=-1
                    else:
                        mode.panda.y=mode.height//3-35
                        mode.panda.x=45
                        mode.scrollX=0
                elif 6*mode.width//5<mode.panda.x<9*mode.width//5:
                    if (mode.cursor[0]+mode.scrollX-80<mode.panda.x\
                        <mode.cursor[0]+mode.scrollX+80):
                        mode.dy*=-1
                    else:
                        mode.panda.y=mode.height//3-35
                        mode.panda.x=45
                        mode.scrollX=0
            elif mode.panda.y<mode.height//3-35:
                mode.panda.y=mode.height//3-35
        else:
            mode.panda.y=mode.height//3-35
    def makePandaVisible(mode):
        if (mode.panda.x > mode.scrollX + mode.width - mode.scrollMarginX):
            mode.scrollX = mode.panda.x - mode.width + mode.scrollMarginX
    def keyPressed(mode, event):
        if (event.key == "h"):
            mode.app.setActiveMode(mode.app.helpModeOne)
        elif (event.key == "a"):
            mode.app.setActiveMode(mode.app.gameModeTwo)
        elif (event.key == "Right"):
            mode.panda.x+=5
            mode.makePandaVisible()
        elif (event.key == "Left"):
            mode.panda.x-=5
            mode.makePandaVisible()
        elif (event.key == "p"):
            mode.isPaused = not mode.isPaused
    def timerFired(mode):
        if (not mode.isPaused):
            mode.panda.panda_timerFired()
            mode.checkBoundary()
            mode.makePandaVisible()
            if mode.panda.x+45>2*mode.width:
                mode.app.setActiveMode(mode.app.mapModeTwo)
    def mouseMoved(mode,event):       
        if event.x+mode.scrollX<mode.width//5:
            mode.cursor=(mode.width//5+50-mode.scrollX,event.y)
            mode.cursorImage=mode.emptyImageCopy
        elif 4*mode.width//5<event.x+mode.scrollX<mode.width:
            mode.cursor=(4*mode.width//5-50-mode.scrollX,event.y)
            mode.cursorImage=mode.emptyImageCopy
        elif mode.width<event.x+mode.scrollX<6*mode.width//5:
            mode.cursor=(6*mode.width//5+50-mode.scrollX,event.y)
            mode.cursorImage=mode.emptyImage
        elif 9*mode.width//5<event.x+mode.scrollX<2*mode.width:
            mode.cursor=(2*mode.width-50-mode.scrollX,event.y)
            mode.cursorImage=mode.emptyImage
        else:
            mode.cursor = (event.x,event.y)
    def redrawAll(mode, canvas):
        canvas.create_image(mode.width//2-mode.scrollX,mode.height//2.5, 
                            image=ImageTk.PhotoImage(mode.bgImage))
        canvas.create_image(3*mode.width//2-mode.scrollX,mode.height//2.5, 
                            image=ImageTk.PhotoImage(mode.bgImageTwo))                  
        cx, cy = mode.panda.x, mode.panda.y
        cx -= mode.scrollX
        mode.panda.panda_redrawAll(canvas,cx,cy)
        canvas.create_rectangle(mode.width//5-mode.scrollX-20, 2*mode.height//3, 
                    4*mode.width//5-mode.scrollX+20,mode.height,fill='light blue')
        canvas.create_rectangle(6*mode.width//5-mode.scrollX-20, 2*mode.height//3, 
                    9*mode.width//5-mode.scrollX+20,mode.height,fill='light blue')
        canvas.create_image(-mode.scrollX,mode.height//1.3, 
                            image=ImageTk.PhotoImage(mode.cliffImage))
        canvas.create_image(mode.width-mode.scrollX,mode.height//1.3, 
                            image=ImageTk.PhotoImage(mode.cliffImage))
        canvas.create_image(2*mode.width-mode.scrollX,mode.height//1.3, 
                            image=ImageTk.PhotoImage(mode.cliffImage))
        canvas.create_rectangle(11*mode.width//5-20, 2*mode.height//3, 
                                14*mode.width//5+20,mode.height,fill='light blue')
        curX,curY = mode.cursor
        canvas.create_image(curX,2*mode.height//3, 
                            image=ImageTk.PhotoImage(mode.cursorImage))

class GameModeTwo(Mode):
    def appStarted(mode):
        urlRocket = 'https://i.loli.net/2019/11/24/Wo2uBZxpygFQvGH.png'
        spritestripRocket0 = mode.loadImage(urlRocket)
        spritestripRocket = mode.scaleImage(spritestripRocket0, 1/10)
        mode.bigPandaImage = mode.scaleImage(spritestripRocket0, 1/6)
        mode.pandaImage= spritestripRocket
        mode.pandaX = mode.width//2 # panda's center
        mode.pandaY = mode.height-20*2 # panda's center
        mode.panda = NewPanda(mode.pandaX,mode.pandaY,mode.pandaImage)
        urlWood = 'https://i.loli.net/2019/11/24/fHiR7lzkC2yvcbN.png'
        spritestripWood0 = mode.loadImage(urlWood)
        spritestripWood = mode.scaleImage(spritestripWood0, 1/10)
        urlOpenBox = 'https://i.loli.net/2019/11/26/xPTSGtAlHy6CWnE.png'
        spritestripOpenBox0 = mode.loadImage(urlOpenBox)
        spritestripOpenBox = mode.scaleImage(spritestripOpenBox0, 1/15)
        mode.bambooImage = spritestripOpenBox 
        urlLife = 'https://i.loli.net/2019/12/01/Dd3lugIpmTnVvU6.png'
        spritestripLife0 = mode.loadImage(urlLife)
        spritestripLife = mode.scaleImage(spritestripLife0, 1/10)
        mode.lifeImage = spritestripLife
        urlEmpty = 'https://i.loli.net/2019/11/30/b4WO8JmcQlxwrBI.png'
        spritestripEmpty0 = mode.loadImage(urlEmpty)
        spritestripEmpty = mode.scaleImage(spritestripEmpty0, 1/20)
        mode.emptyImage = spritestripEmpty    
        urlFire = 'https://i.loli.net/2019/10/26/H9P5CpohNSRE4Z7.png'
        spritestripFire0 = mode.loadImage(urlFire)
        spritestripFire = mode.scaleImage(spritestripFire0, 2/3)
        mode.spritesFire = []
        for i in range(4):
            sprite = spritestripFire.crop((48*i, 48*i, 48*(i+1), 48*(i+1)))
            mode.spritesFire.append(sprite)
        mode.fireY = mode.height//2 
        mode.fireList = []
        for x in [45,mode.width//2,mode.width-45]:
            mode.fireList.append(Fire(mode.spritesFire,x,mode.fireY))
        mode.cellSize=20
        mode.margin=20
        mode.rows=(mode.height-mode.margin*2)//mode.cellSize
        mode.cols=(mode.width-mode.margin*2)//mode.cellSize
        mode.drow=0
        mode.dcol=0
        boardList=[]
        mode.emptyColor="light blue"
        for row in range(mode.rows):
            rowList=[]
            for col in range(mode.cols):
                rowList.append(mode.emptyColor)
            boardList.append(rowList) 
        mode.board=boardList
        mode.brickList=[]
        for row in range((mode.rows-10),(mode.rows-5)):
            col=random.randrange(mode.cols)
            mode.brickList.append(Brick(col,row))
        mode.woodList=[]
        for row in range((mode.rows-19),(mode.rows-13)):
            col=random.randrange(mode.cols)
            mode.woodList.append(Wood(col,row,spritestripWood))
            mode.woodList.append(Wood(col+10,row,spritestripWood))
            mode.woodList.append(Wood(col+30,row,spritestripWood))    
        mode.score=0
        mode.app.timerDelay=200
        mode.isPaused=False
        mode.liveCenterList=[(mode.width-100,mode.height-50),
                            (mode.width-70,mode.height-50),
                            (mode.width-40,mode.height-50)]
        mode.arrivedPanda=[]
        mode.click=0  
    def checkBrickCollision(mode):
        for brick in mode.brickList:
            distanceX = abs(mode.panda.x-brick.x)
            distanceY = abs(mode.panda.y-brick.y)
            if ((mode.panda.newPandaWidth+mode.cellSize)/2-20 <distanceX <= \
                    (mode.panda.newPandaWidth+mode.cellSize)/2 \
                and (distanceY<=(mode.panda.newPandaHeight+mode.cellSize)/2)):
                if mode.liveCenterList!=[]:
                    mode.liveCenterList.pop(0)
                mode.panda.x=mode.width//2
                mode.panda.y=mode.height-20*2
                print(mode.score)    
    def checkWoodCollision(mode):
        for wood in mode.woodList:
            distanceX = abs(mode.panda.x-wood.x)
            distanceY = abs(mode.panda.y-wood.y)
            if distanceX <= (mode.panda.newPandaWidth+mode.cellSize)/2 and\
                distanceY <= (mode.panda.newPandaHeight+mode.cellSize)/2:
                mode.panda.x=wood.x
                mode.panda.y=wood.y
    def checkDestination(mode):   
        if (mode.width//6-30<mode.panda.x<mode.width//6+30 and 
            mode.height//10-20<mode.panda.y<mode.height//10+20):
            mode.score+=20
            mode.arrivedPanda.append((mode.width//6,mode.height//10))
            mode.panda.x=mode.width//2
            mode.panda.y=mode.height-20*2
        elif(mode.width//2-30<mode.panda.x<mode.width//2+30 and 
            mode.height//10-20<mode.panda.y<mode.height//10+20):
            mode.score+=20
            mode.arrivedPanda.append((mode.width//2,mode.height//10))
            mode.panda.x=mode.width//2
            mode.panda.y=mode.height-20*2
        elif(5*mode.width//6-30<mode.panda.x<5*mode.width//6+30 and 
            mode.height//10-20<mode.panda.y<mode.height//10+20):
            mode.score+=20
            mode.arrivedPanda.append((5*mode.width//6,mode.height//10))
            mode.panda.x=mode.width//2
            mode.panda.y=mode.height-20*2             
    def drawCell(mode,canvas,row,col):
        x0 = mode.margin + col * mode.cellSize
        x1 = mode.margin + (col+1) * mode.cellSize
        y0 = mode.margin + row * mode.cellSize
        y1 = mode.margin + (row+1) * mode.cellSize
        canvas.create_rectangle(x0,y0,x1,y1,fill=mode.board[row][col],outline="light blue")
    # draw the brown background
    def drawBg(mode,canvas):
        endX=mode.cols*mode.cellSize+2*mode.margin
        endY=mode.rows*mode.cellSize+2*mode.margin
        canvas.create_rectangle(0,0,endX,endY,fill='brown')
    def drawBoard(mode,canvas):
        for row in range(mode.rows):
            for col in range(mode.cols):
                mode.drawCell(canvas,row,col)
    def isLegalMove(mode):
        if (mode.margin<mode.panda.x<mode.width-mode.margin and 
            mode.margin<mode.panda.y<mode.height-mode.margin):
            return True
        else:
            return False
    def movePanda(mode, dx, dy):
        mode.panda.x += dx
        mode.panda.y += dy
        if not mode.isLegalMove():
            mode.panda.x -= dx
            mode.panda.y -= dy
    def timerFired(mode):
        if (not mode.isPaused):
            mode.checkBrickCollision()
            mode.checkWoodCollision()
            mode.checkDestination()
            for fire in mode.fireList:
                fire.fire_timerFired()
            for brick in mode.brickList:
                brick.brick_timerFired()
            for wood in mode.woodList:
                wood.wood_timerFired()
            if len(mode.arrivedPanda)>=3:
                mode.app.setActiveMode(mode.app.mapModeThree)
            if mode.panda.x>mode.width-20 or mode.panda.x<20:
                mode.liveCenterList.pop(0)
                mode.panda.x=mode.width//2
                mode.panda.y=mode.height-20*2
    def mouseMoved(mode,event):
        mode.cursor = (event.x,event.y)
    def mousePressed(mode,event):
        if 20<event.x<120 and mode.height-90<event.y<mode.height-20:
            mode.isPaused=not mode.isPaused
        elif (mode.height//2-10<event.y<mode.height//2+10 and \
            (35<event.x<55 or mode.width//2-10<event.x<mode.width//2+10 or 
            mode.width-55<event.x<mode.width-35)):
            mode.panda.newPandaImage=mode.bigPandaImage
            mode.click+=1
            if mode.click==3:
                mode.panda.newPandaImage=mode.pandaImage
                mode.click=0
                if mode.fireList!=[]:
                    mode.fireList.pop(0)
    def keyPressed(mode, event):
        if (event.key == "h"):
            mode.app.setActiveMode(mode.app.helpModeTwo)
        elif (event.key == "s"):
            mode.app.setActiveMode(mode.app.mapModeThree)
        elif (event.key == "Left"):    
            mode.movePanda(-30, 0)
        elif (event.key == "Right"): 
            mode.movePanda(+30, 0)
        elif (event.key == "Up"):    
            mode.movePanda(0, -30)
        elif (event.key == "Down"): 
            mode.movePanda(0, +30)
        elif (event.key == "z"): 
            mode.panda.newPandaImage=mode.bigPandaImage
        elif (event.key == "x"): 
            mode.panda.newPandaImage=mode.pandaImage
    def drawDestinations(mode,canvas):
        canvas.create_image(mode.width//6,mode.height//10, 
                            image=ImageTk.PhotoImage(mode.bambooImage))
        canvas.create_image(mode.width//2,mode.height//10, 
                    image=ImageTk.PhotoImage(mode.bambooImage))
        canvas.create_image(5*mode.width//6,mode.height//10, 
                    image=ImageTk.PhotoImage(mode.bambooImage))
    def drawLives(mode,canvas):
        for cx,cy in mode.liveCenterList:
            canvas.create_image(cx,cy,image=ImageTk.PhotoImage(mode.lifeImage))
    def drawArrivedPanda(mode,canvas):
        for cx,cy in mode.arrivedPanda:
            canvas.create_image(cx,cy,image=ImageTk.PhotoImage(mode.pandaImage))
    def drawStopAndContinue(mode,canvas):
        font = 'Arial 20 bold'
        canvas.create_rectangle(20,mode.height-90,120,mode.height-10-10,fill='yellow')
        canvas.create_text(70, mode.height-50-10, text='Stop', font=font)
        canvas.create_rectangle(mode.width-120,mode.height-90,
                                mode.width-20,mode.height-10-10,fill='yellow')
        canvas.create_text(mode.width-70, mode.height-50-30, 
                            text='Lives', font=font)
    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, mode.height,fill='grey')
        cx, cy = mode.panda.x, mode.panda.y
        mode.drawBg(canvas)
        mode.drawBoard(canvas)
        mode.drawDestinations(canvas)
        for fire in mode.fireList:    
            fire.fire_redrawAll(canvas,fire.x,fire.y)
        for brick in mode.brickList:
            brick.brick_redrawAll(canvas)
        for wood in mode.woodList:
            wood.wood_redrawAll(canvas)
        mode.drawStopAndContinue(canvas)
        mode.panda.panda_redrawAll(canvas,cx,cy)
        mode.drawLives(canvas)
        mode.drawArrivedPanda(canvas)
class GameModeThree(Mode):
    def appStarted(mode):
        url = 'https://i.loli.net/2019/11/24/9qpgztci7MUSLBP.png'
        spritestrip0 = mode.loadImage(url)
        spritestrip = mode.scaleImage(spritestrip0, 0.5)
        mode.spritesRight = []
        for i in range(9):
            sprite = spritestrip.crop((89*i, 0, 89*(i+1), 75))
            mode.spritesRight.append(sprite)
        mode.pandaX = 45 # panda's center
        mode.pandaY = mode.height//3-35 # panda's center
        mode.panda = Panda(mode.spritesRight,mode.pandaX,mode.pandaY)
        urlClosedBox = 'https://i.loli.net/2019/12/01/B1azCkhZH6xYdgs.png'
        spritestripClosedBox0 = mode.loadImage(urlClosedBox)
        spritestripClosedBox = mode.scaleImage(spritestripClosedBox0, 1/10)
        mode.bambooImage = spritestripClosedBox
        mode.bambooImageCopy = spritestripClosedBox
        mode.bamboosCenter = [(0.4*mode.width,0.5*mode.height),
                            (0.55*mode.width,0.4*mode.height),
                            (0.55*mode.width,0.6*mode.height),
                            (0.7*mode.width,0.3*mode.height),
                            (0.7*mode.width,0.5*mode.height),
                            (0.7*mode.width,0.7*mode.height),
                            (0.85*mode.width,0.2*mode.height),
                            (0.85*mode.width,0.4*mode.height),
                            (0.85*mode.width,0.6*mode.height),
                            (0.85*mode.width,0.8*mode.height)]
        urlBow = 'https://i.loli.net/2019/11/29/zs6P4JBOEfxKR3q.png'
        spritestripBow0 = mode.loadImage(urlBow)
        spritestripBow = mode.scaleImage(spritestripBow0, 1/20)
        mode.bowImageCopy = spritestripBow
        mode.bowImage = spritestripBow
        mode.bowX=mode.width//5
        mode.bowY=mode.height//3
        urlArrow = 'https://i.loli.net/2019/11/29/dikITGFMc7qr5Yn.png' 
        spritestripArrow0 = mode.loadImage(urlArrow)
        spritestripArrow = mode.scaleImage(spritestripArrow0, 1/20)
        mode.arrowImage = spritestripArrow
        mode.arrowImageCopy = spritestripArrow
        mode.arrowX= mode.width//5
        mode.arrowY= mode.height//3
        urlEmpty = 'https://i.loli.net/2019/11/30/b4WO8JmcQlxwrBI.png'
        spritestripEmpty0 = mode.loadImage(urlEmpty)
        spritestripEmpty = mode.scaleImage(spritestripEmpty0, 1/20)
        mode.emptyImage = spritestripEmpty
        mode.cursor =(0,0)
        mode.margin = 10
        mode.dx=30
        mode.dy=0
        mode.moseIsReleased=False
        mode.dtheta=1
        mode.angle=0
        mode.distance=0
        mode.score=0
        mode.targetPosition=[(0,0)]
        mode.shouldPandaMove=False
        mode.pandaDx=1
        mode.pandaDy=1
        mode.startX=mode.bowX
        mode.startY=mode.bowY
        mode.isPaused=False
    def calculateAngle(mode,x1,y1,x2,y2):
        angle = 0.0
        dx = x2-x1
        dy = y2-y1
        if  x2 == x1:
            angle = math.pi/2.0
        if  y2 == y1 :
            angle = 0.0
        elif y2 < y1 :
            angle = 3.0*math.pi/2.0
        elif x2 > x1 and y2 > y1:
            angle = math.atan(dx/dy)
        elif  x2 > x1 and  y2 < y1 :
            angle = math.pi/2+math.atan(-dy/dx)
        elif  x2 < x1 and y2 < y1 :
            angle = math.pi+math.atan(dx/dy)
        elif  x2 < x1 and y2 > y1 :
            angle = 3.0*math.pi/2.0+math.atan(dy/-dx)
        return angle
    def checkArrowInBoard(mode):
        if mode.arrowX>mode.width or mode.arrowY>mode.height:
            mode.arrowX= mode.width//5
            mode.arrowY= mode.height//3
            mode.dx=30
            mode.dy=0
            mode.moseIsReleased=False
    def checkBambooCollision(mode):
        for cx,cy in mode.bamboosCenter:
            if(cx-20<mode.arrowX<cx+20 and cy-20<mode.arrowY<cy+20):
                mode.targetPosition.append((cx,cy))               
        if mode.targetPosition!=[]:
            mode.emptyImage=mode.arrowImageCopy
        print(mode.targetPosition)
    def eatBamboo(mode):
        if len(mode.targetPosition)>1:
            mode.shouldPandaMove=True
            x,y=mode.targetPosition[1]
            mode.pandaDx=(x-mode.startX)//20
            mode.pandaDy=(y-mode.startY)//20
            print(mode.pandaDx,mode.pandaDy)
    def updateTargetPosition(mode):
        x,y=mode.targetPosition[1]
        if x-50<mode.panda.x<x+50 and y-50<mode.panda.y<y+50:
            mode.score+=1
            mode.panda.x=x
            mode.panda.y=y
            mode.targetPosition.pop(1)
            mode.bamboosCenter.remove((x,y))
    def hasPandaEaten(mode):
        if len(mode.bamboosCenter)<=10:
            mode.shouldPandaMove=False
            mode.startX=mode.panda.x
            mode.startY=mode.panda.y
    def timerFired(mode):
        if (not mode.isPaused):
            if mode.score<=3:
                mode.panda.panda_timerFired()
                if mode.moseIsReleased==True:
                    mode.arrowX+=mode.dx
                    mode.arrowY+=mode.dy
                    mode.dy+=2
                mode.checkArrowInBoard()
                mode.checkBambooCollision()
                mode.eatBamboo()
                if mode.shouldPandaMove==True:
                    mode.panda.x+=mode.pandaDx
                    mode.panda.y+=mode.pandaDy
                    mode.updateTargetPosition()
                    print(mode.panda.x,mode.panda.y)
                mode.hasPandaEaten()
            else:
                mode.app.setActiveMode(mode.app.gameWinMode)
    def keyPressed(mode, event):
        if (event.key == "h"):
            mode.app.setActiveMode(mode.app.helpModeThree)
        elif (event.key == "p"):
            mode.isPaused = not mode.isPaused
    def calculateVelocity(mode,ex,ey):
        dis=math.sqrt((ex-mode.bowX)**2+(ey-mode.bowY)**2)
        mode.angle=mode.calculateAngle(mode.bowX, mode.bowY, ex, ey)
        if 0<mode.angle* 180 / math.pi<90:
            mode.dy=-dis//30
        elif 270<mode.angle* 180 / math.pi<360:
            mode.dy=dis//30
    def mouseDragged(mode,event):
        mode.angle=mode.calculateAngle(mode.bowX, mode.bowY, event.x, event.y)
        img1=mode.bowImageCopy.rotate(mode.angle * 180 / math.pi)
        mode.bowImage=img1
        img2=mode.arrowImageCopy.rotate(mode.angle * 180 / math.pi)
        mode.arrowImage=img2
        mode.distance=math.sqrt((event.x-mode.bowX)**2+(event.y-mode.bowY)**2)
    def mouseReleased(mode,event):
        print(mode.angle* 180 / math.pi)
        mode.bowImage=mode.bowImageCopy
        mode.arrowImage=mode.arrowImageCopy
        mode.moseIsReleased=True
        mode.calculateVelocity(event.x,event.y)
    def showDistanceAndScore(mode,canvas):
        font = 'Arial 20 bold'
        canvas.create_rectangle(20,20,150,90,fill='yellow')
        canvas.create_text(85, 55, text=f'distance:{int(mode.distance)}', font=font)
        canvas.create_rectangle(20,mode.height-90,120,mode.height-10-10,fill='yellow')
        canvas.create_text(70, mode.height-50-10, text=f'score:{mode.score}', font=font)
    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, mode.height,fill='brown')
        canvas.create_rectangle(mode.margin, mode.margin, mode.width-mode.margin, 
                                mode.height-mode.margin,fill='light yellow')
        for cx,cy in mode.bamboosCenter:
            canvas.create_image(cx,cy, 
                            image=ImageTk.PhotoImage(mode.bambooImage))
        canvas.create_image(mode.bowX,mode.bowY, 
                            image=ImageTk.PhotoImage(mode.bowImage))
        canvas.create_image(mode.arrowX,mode.arrowY, 
                            image=ImageTk.PhotoImage(mode.arrowImage))
        px, py = mode.panda.x, mode.panda.y
        mode.panda.panda_redrawAll(canvas,px,py)
        for ax,ay in mode.targetPosition:
            canvas.create_image(ax,ay,image=ImageTk.PhotoImage(mode.emptyImage))       
        mode.showDistanceAndScore(canvas)
class GameOverMode(Mode):
    def redrawAll(mode, canvas):
        font = 'Arial 26 bold'
        canvas.create_text(mode.width/2, 150, text='You lose!', font=font)
        canvas.create_text(mode.width/2, 350, text='Press r to return to the game!', font=font)
    def keyPressed(mode, event):
        if event.key == "r":
            mode.app.splashScreenMode.appStarted()
            mode.app.setActiveMode(mode.app.splashScreenMode)

class GameWinMode(Mode):
    def appStarted(mode):
        url = 'https://i.loli.net/2019/11/24/9qpgztci7MUSLBP.png'
        spritestrip0 = mode.loadImage(url)
        spritestrip = mode.scaleImage(spritestrip0, 0.5)
        mode.spritesRight = []
        for i in range(9):
            sprite = spritestrip.crop((89*i, 0, 89*(i+1), 75))
            mode.spritesRight.append(sprite)
        mode.pandaX = 45 # panda's center
        mode.pandaY = mode.height//3-35 # panda's center
        mode.panda = Panda(mode.spritesRight,mode.pandaX,mode.pandaY)
        mode.dy=0
        urlBackground = 'https://i.loli.net/2019/12/06/Pk7b5hrNFs2WfEd.png'
        spritestripBg0 = mode.loadImage(urlBackground)
        spritestripBg = mode.scaleImage(spritestripBg0, 1/6)
        mode.bgImage = spritestripBg
    def checkBoundary(mode):
        mode.panda.y+=mode.dy
        mode.dy+=3
        if mode.panda.y>mode.height-50:
            mode.dy*=-1
        elif mode.panda.y<mode.height//3-35:
            mode.panda.y=mode.height//3-35
    def timerFired(mode):
        mode.panda.panda_timerFired()
        mode.checkBoundary()
    # key frame from course notes
    # http://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
    def keyPressed(mode, event):
        if event.key == "r":
            mode.app.splashScreenMode.appStarted()
            mode.app.setActiveMode(mode.app.splashScreenMode)
    def redrawAll(mode, canvas):
        canvas.create_rectangle(0,0,mode.width,mode.height,fill='pink')
        canvas.create_image(mode.width//2,mode.height//2, 
                            image=ImageTk.PhotoImage(mode.bgImage))
        cx, cy = mode.panda.x, mode.panda.y
        mode.panda.panda_redrawAll(canvas,cx,cy)
        font = 'Arial 26 bold'
        canvas.create_text(mode.width/2, 150, text='You win!', font=font)
        canvas.create_text(mode.width/2, 350, text='Press r to return to the game!', font=font)
class MapModeOne(Mode):
    def appStarted(mode):
        mapUrl = 'https://i.loli.net/2019/11/30/dZTAq3hU4MeWf9s.png'
        mapSpritestrip0 = mode.loadImage(mapUrl)
        mapSpritestrip = mode.scaleImage(mapSpritestrip0, 0.65)
        mode.mapImage = mapSpritestrip
        lockUrl = 'https://i.loli.net/2019/11/30/94HYauhWTZoOMSE.png'
        lockSpritestrip0 = mode.loadImage(lockUrl)
        lockSpritestrip = mode.scaleImage(lockSpritestrip0, 0.06)
        mode.lockImage = lockSpritestrip
        url = 'https://i.loli.net/2019/11/24/9qpgztci7MUSLBP.png'
        spritestrip0 = mode.loadImage(url)
        spritestrip = mode.scaleImage(spritestrip0, 0.5)
        mode.spritesRight = []
        for i in range(9):
            sprite = spritestrip.crop((89*i, 0, 89*(i+1), 75))
            mode.spritesRight.append(sprite)
        mode.pandaX = 50 # panda's center
        mode.pandaY = mode.height-45 # panda's center
        mode.panda = Panda(mode.spritesRight,mode.pandaX,mode.pandaY)
        mode.shouldPandaMove=False
    def movePanda(mode):
        mode.panda.x+=10
    def mousePressed(mode,event):
        if (mode.panda.x-30<event.x<mode.panda.x+30 and 
            mode.panda.y-30<event.y<mode.panda.y+30):
            mode.shouldPandaMove=True
        elif(2*mode.width//3-50<event.x<2*mode.width//3+10 and 
            mode.height-100<event.y<mode.height-40):
            mode.app.setActiveMode(mode.app.gameModeOne)
        elif (mode.width-100<=event.x<=mode.width-10  and 
            mode.height-90<=event.y<=mode.height-10) :
            mode.app.setActiveMode(mode.app.helpModeTwo)      
    def timerFired(mode):
        mode.panda.panda_timerFired()
        if mode.shouldPandaMove==True:
            mode.movePanda()
            if (2*mode.width//3-20<mode.panda.x<2*mode.width//3+20):
                mode.shouldPandaMove=False
                mode.panda.x = 2*mode.width//3
    def drawStops(mode,canvas):        
        font = 'Arial 20 bold'
        canvas.create_oval(2*mode.width//3-30,mode.height//3-30,
                            2*mode.width//3+30,mode.height//3+30,fill='light yellow')
        canvas.create_oval(mode.width//3-30,mode.height//2-30,
                            mode.width//3+30,mode.height//2+30,fill='light yellow')
        canvas.create_oval(2*mode.width//3-50,mode.height-100,
                            2*mode.width//3+10,mode.height-40,fill='light yellow')
        canvas.create_text(2*mode.width//3-20,mode.height-70, text='Jump', font=font)
        canvas.create_image(2*mode.width//3,mode.height//3, 
                            image=ImageTk.PhotoImage(mode.lockImage))
        canvas.create_image(mode.width//3,mode.height//2, 
                            image=ImageTk.PhotoImage(mode.lockImage))
    def redrawAll(mode,canvas):
        canvas.create_image(mode.width//2,mode.height//2, 
                            image=ImageTk.PhotoImage(mode.mapImage))
        mode.drawStops(canvas)
        cx, cy = mode.panda.x, mode.panda.y
        mode.panda.panda_redrawAll(canvas,cx,cy)
        canvas.create_oval(mode.width-100,mode.height-90,
                                mode.width-10,mode.height-10,fill='pink')
        canvas.create_text(mode.width-55,mode.height-50,text='HELP',font ='Arial 20 bold')
class MapModeTwo(Mode):
    def appStarted(mode):
        mapUrl = 'https://i.loli.net/2019/11/30/dZTAq3hU4MeWf9s.png'
        mapSpritestrip0 = mode.loadImage(mapUrl)
        mapSpritestrip = mode.scaleImage(mapSpritestrip0, 0.65)
        mode.mapImage = mapSpritestrip
        lockUrl = 'https://i.loli.net/2019/11/30/94HYauhWTZoOMSE.png'
        lockSpritestrip0 = mode.loadImage(lockUrl)
        lockSpritestrip = mode.scaleImage(lockSpritestrip0, 0.06)
        mode.lockImage = lockSpritestrip
        url = 'https://i.loli.net/2019/11/30/nzEGIW9sCwRyhDK.png'
        spritestrip0 = mode.loadImage(url)
        spritestrip = mode.scaleImage(spritestrip0, 0.5)
        mode.spritesRight = []
        for i in range(9):
            sprite = spritestrip.crop((89*i, 0, 89*(i+1), 75))
            mode.spritesRight.append(sprite)
        mode.pandaX = 2*mode.width//3 # panda's center
        mode.pandaY = mode.height-45 # panda's center
        mode.panda = Panda(mode.spritesRight,mode.pandaX,mode.pandaY)
        mode.shouldPandaMove=False
    def movePanda(mode):
        mode.panda.x-=10
        mode.panda.y-=8
    def mousePressed(mode,event):
        if (mode.panda.x-30<event.x<mode.panda.x+30 and 
            mode.panda.y-30<event.y<mode.panda.y+30):
            mode.shouldPandaMove=True
        elif(mode.width//3-50<event.x<mode.width//3+50 and 
            mode.height//2-50<event.y<mode.height//2+50):
            mode.app.setActiveMode(mode.app.gameModeTwo)
        elif (mode.width-100<=event.x<=mode.width-10  and 
            mode.height-90<=event.y<=mode.height-10) :
            mode.app.setActiveMode(mode.app.helpModeThree)    
    def timerFired(mode):
        mode.panda.panda_timerFired()
        if mode.shouldPandaMove==True:
            mode.movePanda()
            if (mode.width//3-50<mode.panda.x<mode.width//3+50 and 
                mode.height//2-50<mode.panda.y<mode.height//2+50):
                mode.shouldPandaMove=False
                mode.panda.x = mode.width//3
                mode.panda.y = mode.height//2+50
    def drawStops(mode,canvas):        
        font = 'Arial 20 bold'
        canvas.create_oval(2*mode.width//3-30,mode.height//3-30,
                            2*mode.width//3+30,mode.height//3+30,fill='light yellow')
        canvas.create_oval(mode.width//3-30,mode.height//2-30,
                            mode.width//3+30,mode.height//2+30,fill='light yellow')
        canvas.create_text(mode.width//3,mode.height//2, text='Cross', font=font)
        canvas.create_oval(2*mode.width//3-50,mode.height-100,
                            2*mode.width//3+10,mode.height-40,fill='light yellow')
        canvas.create_text(2*mode.width//3-20,mode.height-70, text='Jump', font=font)
        canvas.create_image(2*mode.width//3,mode.height//3, 
                            image=ImageTk.PhotoImage(mode.lockImage))
    def redrawAll(mode,canvas):
        canvas.create_image(mode.width//2,mode.height//2, 
                            image=ImageTk.PhotoImage(mode.mapImage))
        mode.drawStops(canvas)
        cx, cy = mode.panda.x, mode.panda.y
        mode.panda.panda_redrawAll(canvas,cx,cy)
        canvas.create_oval(mode.width-100,mode.height-90,
                                mode.width-10,mode.height-10,fill='pink')
        canvas.create_text(mode.width-55,mode.height-50,text='HELP',font ='Arial 20 bold')
class MapModeThree(Mode):
    def appStarted(mode):
        mapUrl = 'https://i.loli.net/2019/11/30/dZTAq3hU4MeWf9s.png'
        mapSpritestrip0 = mode.loadImage(mapUrl)
        mapSpritestrip = mode.scaleImage(mapSpritestrip0, 0.65)
        mode.mapImage = mapSpritestrip
        lockUrl = 'https://i.loli.net/2019/11/30/94HYauhWTZoOMSE.png'
        lockSpritestrip0 = mode.loadImage(lockUrl)
        lockSpritestrip = mode.scaleImage(lockSpritestrip0, 0.06)
        mode.lockImage = lockSpritestrip
        url = 'https://i.loli.net/2019/11/24/9qpgztci7MUSLBP.png'
        spritestrip0 = mode.loadImage(url)
        spritestrip = mode.scaleImage(spritestrip0, 0.5)
        mode.spritesRight = []
        for i in range(9):
            sprite = spritestrip.crop((89*i, 0, 89*(i+1), 75))
            mode.spritesRight.append(sprite)
        mode.pandaX = mode.width//3
        mode.pandaY = mode.height//2+50
        mode.panda = Panda(mode.spritesRight,mode.pandaX,mode.pandaY)
        mode.shouldPandaMove=False
    def movePanda(mode):
        mode.panda.x+=10
        mode.panda.y-=8
    def mousePressed(mode,event):
        if (mode.panda.x-50<event.x<mode.panda.x+50 and 
            mode.panda.y-50<event.y<mode.panda.y+50):
            mode.shouldPandaMove=True
        elif(2*mode.width//3-50<event.x<2*mode.width//3+50 and 
            mode.height//3-50<event.y<mode.height//3+50):
            mode.app.setActiveMode(mode.app.gameModeThree)
        elif (mode.width-100<=event.x<=mode.width-10  and 
            mode.height-90<=event.y<=mode.height-10) :
            mode.app.setActiveMode(mode.app.helpModeFour)    
    def timerFired(mode):
        mode.panda.panda_timerFired()
        if mode.shouldPandaMove==True:
            mode.movePanda()
            if (2*mode.width//3-50<mode.panda.x<2*mode.width//3+50 and 
                mode.height//3-50<mode.panda.y<mode.height//3+50):
                mode.shouldPandaMove=False
                mode.panda.x = 2*mode.width//3
                mode.panda.y = mode.height//3+50
    def drawStops(mode,canvas):        
        font = 'Arial 20 bold'
        canvas.create_oval(2*mode.width//3-30,mode.height//3-30,
                            2*mode.width//3+30,mode.height//3+30,fill='light yellow')
        canvas.create_oval(mode.width//3-30,mode.height//2-30,
                            mode.width//3+30,mode.height//2+30,fill='light yellow')
        canvas.create_text(mode.width//3,mode.height//2, text='Cross', font=font)
        canvas.create_oval(2*mode.width//3-50,mode.height-100,
                            2*mode.width//3+10,mode.height-40,fill='light yellow')
        canvas.create_text(2*mode.width//3-20,mode.height-70, text='Jump', font=font)
        canvas.create_text(2*mode.width//3,mode.height//3, text='Shoot', font=font)
    def redrawAll(mode,canvas):
        canvas.create_image(mode.width//2,mode.height//2, 
                            image=ImageTk.PhotoImage(mode.mapImage))
        mode.drawStops(canvas)
        cx, cy = mode.panda.x, mode.panda.y
        mode.panda.panda_redrawAll(canvas,cx,cy)
        canvas.create_oval(mode.width-100,mode.height-90,
                                mode.width-10,mode.height-10,fill='pink')
        canvas.create_text(mode.width-55,mode.height-50,text='HELP',font ='Arial 20 bold')
class HelpModeOne(Mode):
    def appStarted(mode):
        urlRocket = 'https://i.loli.net/2019/11/24/Wo2uBZxpygFQvGH.png'
        spritestripRocket0 = mode.loadImage(urlRocket)
        spritestripRocket = mode.scaleImage(spritestripRocket0, 1/10)
        mode.pandaImage= spritestripRocket
        bgHelpUrl = 'https://i.loli.net/2019/12/05/6vgnpJMK3xRDb1O.png'
        mapSpritestrip0 = mode.loadImage(bgHelpUrl)
        mapSpritestrip = mode.scaleImage(mapSpritestrip0, 1.6)
        mode.bgHelpImage = mapSpritestrip
        mode.squareLeft = mode.width//2
        mode.squareTop = mode.height//2
        mode.squareSize = 25
        mode.dx = 10
        mode.dy = 15
        mode.timerDelay=50
    def timerFired(mode):
        mode.doStep()
    def doStep(mode):
        mode.squareLeft += mode.dx
        if mode.squareLeft < 0:
            mode.squareLeft = 0
            mode.dx = -mode.dx
        elif mode.squareLeft > mode.width - mode.squareSize:
            mode.squareLeft = mode.width - mode.squareSize
            mode.dx = -mode.dx
        mode.squareTop += mode.dy
        if mode.squareTop < 0:
            mode.squareTop = 0
            mode.dy = -mode.dy
        elif mode.squareTop > mode.height - mode.squareSize:
            mode.squareTop = mode.height - mode.squareSize
            mode.dy = -mode.dy
    def keyPressed(mode, event):
        if event.key=='r':
            mode.app.setActiveMode(mode.app.splashScreenMode)
    def redrawAll(mode, canvas):
        canvas.create_image(mode.width//2,mode.height//2, 
                            image=ImageTk.PhotoImage(mode.bgHelpImage))

        canvas.create_image(mode.squareLeft+ mode.squareSize//2,
                            mode.squareTop + mode.squareSize//2,
                            image=ImageTk.PhotoImage(mode.pandaImage))
        font = 'Arial 26 bold'
        canvas.create_text(mode.width/2+25, 100, 
        text='There are 3 steps in total\nFollow the map between each step', font=font)
        canvas.create_text(mode.width/2, 200, 
        text='Arrows to move, \nMouse to move, click and drag', font=font)
        canvas.create_text(mode.width/2+5,300,
                            text='Press p or click "stop" for stop', font=font)
        canvas.create_text(mode.width/2+5,450,
                            text='Press r to return to Main Menu', font=font)
class HelpModeTwo(Mode):
    def appStarted(mode):
        urlRocket = 'https://i.loli.net/2019/11/24/Wo2uBZxpygFQvGH.png'
        spritestripRocket0 = mode.loadImage(urlRocket)
        spritestripRocket = mode.scaleImage(spritestripRocket0, 1/10)
        mode.pandaImage= spritestripRocket
        bgHelpUrl = 'https://i.loli.net/2019/12/05/SMRD9LUaVgmCwlB.png'
        mapSpritestrip0 = mode.loadImage(bgHelpUrl)
        mapSpritestrip = mode.scaleImage(mapSpritestrip0, 1.25)
        mode.bgHelpImage = mapSpritestrip
        mode.squareLeft = mode.width//2
        mode.squareTop = mode.height//2
        mode.squareSize = 25
        mode.dx = 10
        mode.dy = 15
        mode.timerDelay=50
    def timerFired(mode):
        mode.doStep()
    def doStep(mode):
        mode.squareLeft += mode.dx
        if mode.squareLeft < 0:
            mode.squareLeft = 0
            mode.dx = -mode.dx
        elif mode.squareLeft > mode.width - mode.squareSize:
            mode.squareLeft = mode.width - mode.squareSize
            mode.dx = -mode.dx
        mode.squareTop += mode.dy
        if mode.squareTop < 0:
            mode.squareTop = 0
            mode.dy = -mode.dy
        elif mode.squareTop > mode.height - mode.squareSize:
            mode.squareTop = mode.height - mode.squareSize
            mode.dy = -mode.dy
    def keyPressed(mode, event):
        if event.key=='r':
            mode.app.setActiveMode(mode.app.mapModeOne)
    def redrawAll(mode, canvas):
        canvas.create_image(mode.width//2,mode.height//2, 
                            image=ImageTk.PhotoImage(mode.bgHelpImage))

        canvas.create_image(mode.squareLeft+ mode.squareSize//2,
                            mode.squareTop + mode.squareSize//2,
                            image=ImageTk.PhotoImage(mode.pandaImage))
        font = 'Arial 26 bold'
        canvas.create_text(mode.width/2-25, 100, 
        text='Step 1: Jump across the river',font=font)
        canvas.create_text(mode.width/2, 200, 
        text='Arrows to move panda, \nMouse to move object in the water', font=font)
        canvas.create_text(mode.width/2+5,275,
                            text='Click panda and then click Jump', font=font)
        canvas.create_text(mode.width/2+5,350,
                            text='Press p to pause during this step', font=font)
        canvas.create_text(mode.width/2+5,450,
                            text='Press r to return to Map', font=font)
class HelpModeThree(Mode):
    def appStarted(mode):
        urlRocket = 'https://i.loli.net/2019/11/24/Wo2uBZxpygFQvGH.png'
        spritestripRocket0 = mode.loadImage(urlRocket)
        spritestripRocket = mode.scaleImage(spritestripRocket0, 1/10)
        mode.pandaImage= spritestripRocket
        bgHelpUrl = 'https://i.loli.net/2019/12/05/SMRD9LUaVgmCwlB.png'
        mapSpritestrip0 = mode.loadImage(bgHelpUrl)
        mapSpritestrip = mode.scaleImage(mapSpritestrip0, 1.25)
        mode.bgHelpImage = mapSpritestrip
        mode.squareLeft = mode.width//2
        mode.squareTop = mode.height//2
        mode.squareSize = 25
        mode.dx = 10
        mode.dy = 15
        mode.timerDelay=50
    def timerFired(mode):
        mode.doStep()
    def doStep(mode):
        mode.squareLeft += mode.dx
        if mode.squareLeft < 0:
            mode.squareLeft = 0
            mode.dx = -mode.dx
        elif mode.squareLeft > mode.width - mode.squareSize:
            mode.squareLeft = mode.width - mode.squareSize
            mode.dx = -mode.dx
        mode.squareTop += mode.dy
        if mode.squareTop < 0:
            mode.squareTop = 0
            mode.dy = -mode.dy
        elif mode.squareTop > mode.height - mode.squareSize:
            mode.squareTop = mode.height - mode.squareSize
            mode.dy = -mode.dy
    def keyPressed(mode, event):
        if event.key=='r':
            mode.app.setActiveMode(mode.app.mapModeTwo)
    def redrawAll(mode, canvas):
        canvas.create_image(mode.width//2,mode.height//2, 
                            image=ImageTk.PhotoImage(mode.bgHelpImage))

        canvas.create_image(mode.squareLeft+ mode.squareSize//2,
                            mode.squareTop + mode.squareSize//2,
                            image=ImageTk.PhotoImage(mode.pandaImage))
        font = 'Arial 26 bold'
        canvas.create_text(mode.width/2-50, 100, 
        text='Step 2: Cross all the obstacles',font=font)
        canvas.create_text(mode.width/2, 200, 
        text='Arrows to move panda, \nMouse click to eliminate the fire', font=font)
        canvas.create_text(mode.width/2+5,275,
                            text='Click panda and then click Cross', font=font)
        canvas.create_text(mode.width/2+5,350,
                            text='Click stop to pause during this step', font=font)
        canvas.create_text(mode.width/2+5,450,
                            text='Press r to return to Map', font=font)
class HelpModeFour(Mode):
    def appStarted(mode):
        urlRocket = 'https://i.loli.net/2019/11/24/Wo2uBZxpygFQvGH.png'
        spritestripRocket0 = mode.loadImage(urlRocket)
        spritestripRocket = mode.scaleImage(spritestripRocket0, 1/10)
        mode.pandaImage= spritestripRocket
        bgHelpUrl = 'https://i.loli.net/2019/12/05/SMRD9LUaVgmCwlB.png'
        mapSpritestrip0 = mode.loadImage(bgHelpUrl)
        mapSpritestrip = mode.scaleImage(mapSpritestrip0, 1.25)
        mode.bgHelpImage = mapSpritestrip
        mode.squareLeft = mode.width//2
        mode.squareTop = mode.height//2
        mode.squareSize = 25
        mode.dx = 10
        mode.dy = 15
        mode.timerDelay=50
    def timerFired(mode):
        mode.doStep()
    def doStep(mode):
        mode.squareLeft += mode.dx
        if mode.squareLeft < 0:
            mode.squareLeft = 0
            mode.dx = -mode.dx
        elif mode.squareLeft > mode.width - mode.squareSize:
            mode.squareLeft = mode.width - mode.squareSize
            mode.dx = -mode.dx
        mode.squareTop += mode.dy
        if mode.squareTop < 0:
            mode.squareTop = 0
            mode.dy = -mode.dy
        elif mode.squareTop > mode.height - mode.squareSize:
            mode.squareTop = mode.height - mode.squareSize
            mode.dy = -mode.dy
    def keyPressed(mode, event):
        if event.key=='r':
            mode.app.setActiveMode(mode.app.mapModeThree)
    def redrawAll(mode, canvas):
        canvas.create_image(mode.width//2,mode.height//2, 
                            image=ImageTk.PhotoImage(mode.bgHelpImage))

        canvas.create_image(mode.squareLeft+ mode.squareSize//2,
                            mode.squareTop + mode.squareSize//2,
                            image=ImageTk.PhotoImage(mode.pandaImage))
        font = 'Arial 26 bold'
        canvas.create_text(mode.width/2-50, 100, 
        text='Step 3: Shoot the bamboos',font=font)
        canvas.create_text(mode.width/2, 200,    
        text='Mouse press and release for shooting', font=font)
        canvas.create_text(mode.width/2+5,275,
                            text='The panda can eat by itself', font=font)
        canvas.create_text(mode.width/2+5,350,
                            text='Shoot over 3 bamboos to win the whole game', font=font)
        canvas.create_text(mode.width/2+5,450,
                            text='Press r to return to Map', font=font)
class MyModalApp(ModalApp):
    def appStarted(app):
        app.splashScreenMode = SplashScreenMode()
        app.mapModeOne = MapModeOne()
        app.gameModeOne = GameModeOne()
        app.mapModeTwo = MapModeTwo()
        app.gameModeTwo = GameModeTwo()
        app.mapModeThree = MapModeThree()
        app.gameModeThree = GameModeThree()
        app.helpModeOne = HelpModeOne()
        app.helpModeTwo = HelpModeTwo()
        app.helpModeThree = HelpModeThree()
        app.helpModeFour = HelpModeFour()
        app.gameOverMode = GameOverMode()
        app.gameWinMode = GameWinMode()
        app.setActiveMode(app.splashScreenMode)
        app.timerDelay = 50
app = MyModalApp(width=500, height=500)

    