import cv2
import numpy

#cProgramScreen should handle all the drawing, and event control
#You need to modify the cProgramScreen.
class cProgramScreen: 
    #ScreenParameters
    mcScreenWidth=600#WidthOfTheProgram
    mcScreenHeight=600#HeightOftheProgram
    mcTitle="DrawingProgram"#NameOftheScreenForDrawing
    mDisplayImage=None#WhereEverythingGetsDrawn
    mPressedKey=-1#TellsWhichKeyIsPressed
    mCurrentMode="None"#ControlsCurrentDrawingMode_StringIsInefficentForThisButItisModeReadable
    mLineCounter = 0 
    mPrevIx = 0
    mPrevIy = 0
    mTopCornerX = 0
    mTopCornerY = 0
    mRectangleCounter = 0 
    brushing = False
    points = []
    
    def __init__(self):
        cv2.namedWindow(self.mcTitle)
        self.fCreateRGBTrackBars()
        cv2.setMouseCallback(self.mcTitle,self.fMouseEvent)#CreatesaCallbackforMouseEvents
        self.fRefreshScreen()#Creates an Empty Screen To Draw On
    #UsedForDrawingTrackBarsToImage
    def fCreateRGBTrackBars(self):
        def fEmptyFunction(vInput):
            pass
        cv2.createTrackbar('R',self.mcTitle,0,255,fEmptyFunction)
        cv2.createTrackbar('G',self.mcTitle,0,255,fEmptyFunction)
        cv2.createTrackbar('B',self.mcTitle,0,255,fEmptyFunction)
    #UsedForGettingSelectedRGBColorFromTrackBars
    def fGetSelectedRGBColor(self):
        vRColor=cv2.getTrackbarPos('R',self.mcTitle)
        vGColor=cv2.getTrackbarPos('G',self.mcTitle)
        vBColor=cv2.getTrackbarPos('B',self.mcTitle)
        oSelectedRGBColor=(vRColor,vGColor,vBColor)
        return oSelectedRGBColor
    #HandlesAllMouseRelatedEvents
    #This Function is where majority of your code goes
    #And Majority Of Drawing
    #This function gets called evertime there is a mouse event, and the execution of this function starts from its beginning. That means there might be multiple of these running in parallel for each event(Mouse movement is event and mouse move gets called every time mouse moves a pixel). So our traditional loop and update structure wont work. You might need different variables to check or control different states of your program.
    #ImportantEventsYouNeedToHandleAre
    #cv2.EVENT_LBUTTONDOWN
    #cv2.EVENT_MOUSEMOVE
    #cv2.EVENT_LBUTTONUP
    #cv2.EVENT_RBUTTONDOWN
    def fMouseEvent(self,iEvent,iX,iY,iFlags,iParameters):
        if(self.mCurrentMode=="None"):
            pass
        if(self.mCurrentMode=="Dot"):
            if(iEvent==cv2.EVENT_LBUTTONDOWN):
                (vR,vG,vB)=self.fGetSelectedRGBColor()
                self.mDisplayImage[iY,iX,:]=[vB,vG,vR]
                self.mDisplayImage[iY+1,iX,:]=[vB,vG,vR]
                self.mDisplayImage[iY,iX+1,:]=[vB,vG,vR]
                self.mDisplayImage[iY-1,iX,:]=[vB,vG,vR]
                self.mDisplayImage[iY,iX-1,:]=[vB,vG,vR]
        if(self.mCurrentMode=="Brush"):
            if (cv2.EVENT_LBUTTONDOWN):
                self.brushing = True
            while(self.brushing):
                if (cv2.EVENT_LBUTTONDOWN):
                    self.brushing=False
                    # break
                (vR,vG,vB)=self.fGetSelectedRGBColor()
                self.mDisplayImage[iY,iX,:]=[vB,vG,vR]
        if(self.mCurrentMode=="Line"):
            # self.mLineCounter = 0
            if(iEvent==cv2.EVENT_LBUTTONDOWN):
                # print(self.mLineCounter)
                if (self.mLineCounter % 2 == 0):
                    self.mLineCounter += 1
                    self.mPrevIx = iX
                    self.mPrevIy= iY
                    # print(self.mLineCounter)
                else:
                    (vR,vG,vB)=self.fGetSelectedRGBColor()
                    # print(self.mPrevIx, iX, self.mPrevIy, iY)
                    slope = (iY - self.mPrevIy)/(iX - self.mPrevIx)
                    counter = 0
                    for i in range(self.mPrevIx, iX):
                            counter += 1
                            self.mDisplayImage[int(counter*slope+iY),i,:]=[vB,vG,vR]
                    self.mLineCounter += 1
                    # print(self.mLineCounter)
        if(self.mCurrentMode=="Rectangle"):
            if(iEvent==cv2.EVENT_LBUTTONDOWN):
                if (self.mRectangleCounter % 2 == 0):
                    self.mTopCornerX = iX
                    self.mTopCornerY = iY
                    self.mRectangleCounter += 1
                else:
                    (vR,vG,vB)=self.fGetSelectedRGBColor()
                    counter = 0
                    for i in range(self.mTopCornerX, iX):
                        counter += 1
                        self.mDisplayImage[iY,i,:]=[vB,vG,vR]
                        self.mDisplayImage[self.mTopCornerY+iY,i,:]=[vB,vG,vR]
                    counter = 0
                    for i in range(self.mTopCornerY, iY):
                        counter += 1
                        self.mDisplayImage[iY+counter,iX,:]=[vB,vG,vR]
                        self.mDisplayImage[iY+counter,self.mTopCornerX,:]=[vB,vG,vR]
                    self.mRectangleCounter += 1
                
        if(self.mCurrentMode=="Polygon"):
            if(iEvent==cv2.EVENT_LBUTTONDOWN):
                (vR,vG,vB)=self.fGetSelectedRGBColor()
                self.points.append([iY, iX])
                if (len(self.points) > 2):
                    for i in range(len(self.points)-1, len(self.points)):
                        slope = abs(self.points[i][0] - self.points[i-1][0])/(self.points[i][1] - self.points[i-1][1])
                        counter = 0
                        for j in range(self.points[i][1], self.points[i-1][1]):
                                counter += 1
                                self.mDisplayImage[int(counter*abs(slope)+iY),j,:]=[vB,vG,vR]
            if(iEvent==cv2.EVENT_RBUTTONDOWN):
                counter =0
                slope = (self.points[0][0] - self.points[len(self.points)-1][0])/(self.points[0][1] - self.points[len(self.points)-1][1])
                for j in range(self.points[0][1], self.points[len(self.points)][1]):
                    counter+=1
                    self.points[0]
                    self.mDisplayImage[int(counter*slope+self.points[i][1]),j,:]=[vB,vG,vR]
                self.points.clear

        if(self.mCurrentMode=="Fill"):
            if(iEvent==cv2.EVENT_LBUTTONDOWN):
                (vR,vG,vB)=self.fGetSelectedRGBColor()
                for i in range(self.mcScreenHeight):
                    for j in range(self.mcScreenWidth):
                        self.mDisplayImage[i,j,:]=[vB,vG,vR]
    #UsedForGettingANewScreenImage
    def fRefreshScreen(self):
        self.mDisplayImage=numpy.zeros((self.mcScreenHeight,self.mcScreenWidth,3),numpy.uint8)
    #UsedForDrawingTextForUserNotification
    def fDrawString(self,iText,iXLocation,iYLocation):
        cv2.putText(self.mDisplayImage,iText,(iXLocation,iYLocation),cv2.FONT_HERSHEY_SIMPLEX,1,self.mTextColor,2)
    #UsedForDisplayingScreen
    def fDisplayScreen(self):
        cv2.imshow(self.mcTitle,self.mDisplayImage)
        vNewKey=cv2.waitKey(1)
        if(vNewKey!=-1):
            self.mPressedKey=vNewKey
    #UsedForLearningPressedKey
    #Returns_-1_IfNoKeyIsPressedYet
    #ResetsPressedKeyTo_-1_AfterReturn
    def fGetPressedKey(self):
        oPressedKey=self.mPressedKey
        self.mPressedKey=-1
        return oPressedKey
    #Used for updating the screen and User input processing.
    def fUpdate(self):
        vCurrentModeText="CurrentMode: "+self.mCurrentMode
        self.fDisplayScreen()# Displays the screen to the user. This line is need to have an display
        vPressedKey=self.fGetPressedKey()#This Line needs to Come after Display Screen to Get if a key is pressed
        #You can use similar if statements to check which keyboard is pressed also read ord() function
        #https://docs.python.org/3/library/functions.html#ord
        #Never checks for special keys, if you need special keys like up arrow button change waitkey to waitKeyEx
        #If you change to waitKeyEx use following codes https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
        if(vPressedKey==ord('q')):#Checks If the q button is pressed on keyboard
            exit()#Exits the program
        elif(vPressedKey==ord('a')):#This will reset The DrawMode To None again
            self.mCurrentMode="None"    
        elif(vPressedKey==ord('e')):#This will Refreshes the screen (Makes everything blank again)
            self.fRefreshScreen()#Creates an Empty Screen To Draw On
        elif(vPressedKey==ord('s')):#This will Draw a Single Dot To the Screen
            self.mCurrentMode="Dot"#We gave you this mode as a sample to look at
        elif(vPressedKey==ord('b')):
            #This Should Allow You To have a brush painting option
            #This brush painting will allow the user to paint using mouse movement
            #You will start painting with the pressing a Left mouse button
            #program needs to keeps painting until the mouse button is freed
            self.mCurrentMode="Brush"
            pass#remove pass when you are done
        elif(vPressedKey==ord('r')):
            #ThisShouldAllowYouToDraw a rectangle to the screen
            #Do not fill inside the rectangle
            #Rectangle needs to wait for two mouse click
            #First mouse click determines the top left corner
            #Second Mouse Click Determines the bottom right corner
            #After second click you can draw the rectangle
            self.mCurrentMode="Rectangle"
            pass#remove pass when you are done
        elif(vPressedKey==ord('l')):
            self.mCurrentMode="Line"
            #This Should Allow You To Draw a line to the screen
            #Line needs to wait two mouse click
            #First mouse click determines the starting point
            #Second Mouse Click Determines the ending point
            #After second click you can draw the line
            pass#remove pass when you are done
        elif(vPressedKey==ord('p')):
            #This Should Allow You To Draw a polygon to the screen
            #Polygon can be in arbitrary sizeq
            #the user will select the points and the program will draw line between them
            #First left mouse click starts the first point of the polygon
            #Consecutive left mouse clicks will add more points to you polygon
            #When you add a point to your polygon you need to draw a line between the previous point and the current point
            #When the user does a right mouse click the polygon drawing gets completed by drawing a line between last point and the first point 
            self.mCurrentMode="Polygon"
            pass #remove pass when you are done
        elif(vPressedKey==ord('f')):
            #This Should Allow You To color fill (Paint Bucket tool) and area
            #Color Region is started with the clicked location and the border of a different color(or the image) whichever comes first.
            #When you select color fill and press mouse button on the screen it should color fill the region that you select with the color that is selected
            #The algorithm that you need to implement here is called floodfill and recursive version of the algorithm wont work in python 
            #For every colorfill you start with a list that contains a single element which is first pixel to color(Mouse click location). 
            #For every pixel location in your list you check up,down,left and right of the pixel locations and add them to you list if they share same color with the pixel that is in your list and they are not in the list already. Afterwards color the pixel location. You do this until there is nothing left in your list.
            
            
            self.mCurrentMode="Fill"
            pass #remove pass when you are done

#Do Not Modify Main Function
#All Your Code Should be In the cProgramScreen class
#***************************************************************************************
def Main():
    vProgramScreen=cProgramScreen()#This line is need to create a Screen For the Program
    #MainProgramLoop
    while(True):
        vProgramScreen.fUpdate() 
#***************************************************************************************
Main()#Calls Main To start The game DO NOT DELETE
