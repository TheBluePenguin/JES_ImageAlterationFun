#Made by Zachary Criswell on December/6/2021
def getAverageColor():
  file = pickAFile()
  picture = makePicture(file)
  r = 0
  b = 0
  g = 0
  totalPixels = (getWidth(picture) * getHeight(picture))
  for x in range (0, getWidth(picture)):
    for y in range (0, getHeight(picture)):
      r = r + getRed(getPixel(picture, x, y))
      b = b + getBlue(getPixel(picture, x, y))
      g = g + getGreen(getPixel(picture, x, y))
      
  r = r/totalPixels
  b = b/totalPixels
  g = g/totalPixels
  
  averageColor = makeColor(r, b, g)
  explore(makeEmptyPicture(100, 100, averageColor))