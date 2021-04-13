# Made by Zachary Criswell on April/4/2021
import random
def imageRandomizer():
# makePicture can be replaced with any picture of your choosing.
  picture = makePicture('C:\Users\zacha\Desktop\School Homework\collage\Niko.jpg')
  for x in range(0, 10):  
      randomizer(picture)
  explore(picture)
  
def randomizer(picture):
  xStart = random.randrange(0, getWidth(picture)-2)
  xEnd = random.randrange(xStart+1, getWidth(picture))
  yStart = random.randrange(0, getHeight(picture)-2)
  yEnd = random.randrange(yStart+1, getHeight(picture))
  xPlacementStart = random.randrange(0, getWidth(picture))
  yPlacementStart = random.randrange(0, getHeight(picture))
  yPlacementRestart = yPlacementStart
  for x in range (xStart,xEnd):
    for y in range (yStart,yEnd):
      sourcePx = getPixel(picture,x,y)
      color = getColor(sourcePx)
      destPx = getPixel(picture,xPlacementStart,yPlacementStart)      
      setColor(destPx,color)         
      yPlacementStart = yPlacementStart + 1       
      if yPlacementStart == getHeight(picture):
        yPlacementStart = 0
    xPlacementStart = xPlacementStart + 1
    if xPlacementStart == getWidth(picture):
      xPlacementStart = 0
    yPlacementStart = yPlacementRestart
  return(picture)
  
