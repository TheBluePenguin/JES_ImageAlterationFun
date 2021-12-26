# Made by Zachary Criswell on December/26/2021
import random
def imageBlocks():
# Selects a picture of your choosing.
  picture = makePicture(pickAFile())
  canvas = makeEmptyPicture(getWidth(picture),getHeight(picture))
  filter(picture, canvas)
  explore(canvas)
  

def filter(picture, canvas):
# Sets block sizes
  widthBlock = getWidth(picture)/8
  heightBlock = getHeight(picture)/8
  
# Matches the number of blocks
  a = 0
  b = 0
  for a in range(0, 8):
    for b in range(0, 8):
    
      #Gets random effect Number
      randomEffect = random.randrange(0, 5)
      #Makes a dark block
      if(randomEffect == 0):
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
      elif(randomEffect == 1):
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
      elif(randomEffect == 2):
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
      elif(randomEffect == 3):
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
  
