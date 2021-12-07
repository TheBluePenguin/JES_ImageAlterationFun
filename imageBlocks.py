# Made by Zachary Criswell on April/4/2021
def imageBlocks():
  file = pickAFile()
  picture = makePicture(file)
  canvas = makeEmptyPicture((getWidth(picture)*2),(getHeight(picture)*2))
  orignal(picture, canvas, (getWidth(canvas)/2), 0)
  downReverseDarken(picture, canvas, 0, (getHeight(canvas)/2))
  downLighten(picture, canvas, (getWidth(canvas)/2), (getHeight(canvas)/2))
  reverseBW(picture, canvas, 0, 0)
  explore(canvas)
  
# places the orginal image onto the right top side of the canvas.
def orignal(picture, canvas, targetX, targetY):
  defaultY = targetY
  defaultX = targetX
  for x in range(0, getWidth(picture)):
    for y in range(0, getHeight(picture)):
      sourcePx = getPixel(picture,x,y)
      color = getColor(sourcePx)
      destPx = getPixel(canvas,targetX, targetY)
      setColor(destPx,color)
      targetY = targetY + 1
    targetX = targetX + 1
    targetY = defaultY     
  return(canvas)
 
# places the reverse, and grayscaled image onto the left top side of the canvas.      
def reverseBW(picture, canvas, targetX, targetY):
  for p in getPixels(picture):
    r = int(getRed(p))
    g = int(getGreen(p))
    b = int(getBlue(p))
    r1=r
    g1=g
    b1=b
    new = (r + g + b)/3
    color= makeColor(new,new,new)
    setColor(p, color)
  defaultY = targetY
  defaultX = targetX
  width = getWidth(picture)
  for x in range(0, width):
    for y in range(0, getHeight(picture)):
      sourcePx = getPixel(picture,x,y)
      imgDirection = getPixel(picture, width - x - 1,y)
      color = getColor(imgDirection)
      destPx = getPixel(canvas,targetX,targetY)
      setColor(destPx,color)
      targetY = targetY + 1
    targetX = targetX + 1
    targetY = defaultY
  return(canvas)
  
  
# places the reversed, upside down, and darkened image onto the left bottom side of the canvas.    
def downReverseDarken(picture, canvas, targetX, targetY):
  defaultY = targetY
  defaultX = targetX
  height = getHeight(picture)
  width = getWidth(picture)
  for x in range(0, width):
    for y in range(0, height):
      sourcePx = getPixel(picture,x,y)
      imgDirection = getPixel(picture, width - x - 1, height - y - 1)
      color = makeDarker(makeDarker(getColor(imgDirection)))
      destPx = getPixel(canvas,targetX,targetY)
      setColor(destPx,color)
      targetY = targetY + 1
    targetX = targetX + 1
    targetY = defaultY
  return(canvas)

# places the upside down, and lightened image onto the right bottom side of the canvas.
def downLighten(picture, canvas, targetX, targetY):
  defaultY = targetY
  defaultX = targetX
  height = getHeight(picture)
  for x in range(0, getWidth(picture)):
    for y in range(0, height):
      sourcePx = getPixel(picture,x,y)
      imgDirection = getPixel(picture, x, height - y - 1)
      color = makeLighter(getColor(imgDirection))
      destPx = getPixel(canvas,targetX,targetY)
      setColor(destPx,color)
      targetY = targetY + 1
    targetX = targetX + 1
    targetY = defaultY
  return(canvas)
  
