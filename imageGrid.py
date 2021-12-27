# Made by Zachary Criswell on December/26/2021
import random
def imageBlocks():
# Selects a picture of your choosing.
  picture = makePicture(pickAFile())
  global blNum
  blNum = requestInteger("Choose the number of blocks youd like the width and height to be set as") 
  canvas = makeEmptyPicture(getWidth(picture),getHeight(picture))
  filter(picture, canvas)
  explore(canvas)

def filter(picture, canvas):
# Sets block sizes
  widthBlock = getWidth(picture)/blNum
  heightBlock = getHeight(picture)/blNum
  
# Matches the number of blocks
  a = 0
  b = 0
  for a in range(0, blNum):
    for b in range(0, blNum):
      
      #Gets random effect Number
      randomEffect = random.randrange(0, 5)
      
      #Makes a dark block
      if(randomEffect == 1):
        for x in range(widthBlock*a, widthBlock*(a+1)):
          for y in range(heightBlock*b, heightBlock*(b+1)):
            sourcePx = getPixel(picture,x,y)
            color = getColor(sourcePx)
            destPx = getPixel(canvas,x,y)
            setColor(destPx,makeDarker(color))
            y = y + 1
          x = x + 1
          y = 0   
      #No effect block
      elif(randomEffect == 2):
        for x in range(widthBlock*a, widthBlock*(a+1)):
          for y in range(heightBlock*b, heightBlock*(b+1)):
            sourcePx = getPixel(picture,x,y)
            color = getColor(sourcePx)
            destPx = getPixel(canvas,x,y)
            setColor(destPx,color)
            y = y + 1
          x = x + 1
          y = 0 
      #Makes a extra light block 
      elif(randomEffect == 3):
        for x in range(widthBlock*a, widthBlock*(a+1)):
          for y in range(heightBlock*b, heightBlock*(b+1)):
            sourcePx = getPixel(picture,x,y)
            color = getColor(sourcePx)
            destPx = getPixel(canvas,x,y)
            setColor(destPx,makeLighter(makeLighter(color)))
            y = y + 1
          x = x + 1
          y = 0 
      #Makes a extra dark block
      elif(randomEffect == 4):
        for x in range(widthBlock*a, widthBlock*(a+1)):
          for y in range(heightBlock*b, heightBlock*(b+1)):
            sourcePx = getPixel(picture,x,y)
            color = getColor(sourcePx)
            destPx = getPixel(canvas,x,y)
            setColor(destPx,makeDarker(makeDarker(color)))
            y = y + 1
          x = x + 1
          y = 0 
      #Makes a light block      
      else:
        for x in range(widthBlock*a, widthBlock*(a+1)):
          for y in range(heightBlock*b, heightBlock*(b+1)):
            sourcePx = getPixel(picture,x,y)
            color = getColor(sourcePx)
            destPx = getPixel(canvas,x,y)
            setColor(destPx,makeLighter(color))
            y = y + 1
          x = x + 1
          y = 0
  a = a + 1
  b = b + 1
