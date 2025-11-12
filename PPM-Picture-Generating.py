def clampValueToRange(value,low,high):
    if value<low:
        return int(low)
    elif value>high:
        return int(high)
    else:
        return int(value)

def returnColor(line):
    b=line.split()
    return [int(b[0]),int(b[1]),int(b[2])]

def returnLocation(line):
    c=line.split()
    return [int(c[3]),int(c[4])]

def locationValid(x,width,y,height):
    a=False
    if x>=0 and y>=0 and x<width and y<height:
        a=True
    return a

def convertPixel(color):
    dict5={}
    dict5['r']=clampValueToRange(color[0],0,255)
    dict5['g']=clampValueToRange(color[1],0,255)
    dict5['b']=clampValueToRange(color[2],0,255)
    return dict5

def positionPixel(x,y,color):
    dict6={}
    dict6['pixel']=color
    dict6['x']=x
    dict6['y']=y
    return dict6

def updateChangeList(pixel, pixelList):
    pixelList.append(pixel)
    return None

def readPixelFile(pixels, filename):
    with open(filename,'r') as f:
        for line in f:
            line=line.strip()
            color_list = returnColor(line)          
            location_list = returnLocation(line)    
            color_dict = convertPixel(color_list)  
            pixel_dict = positionPixel(location_list[0], location_list[1], color_dict)
            updateChangeList(pixel_dict, pixels)

def generateEmptyPicture(width,height):
    emptylist=[]
    for j in range(height):
        inlist=[]
        for i in range(width):
            a={'r': 0, 'g': 0, 'b': 0}
            inlist.append(a)
        emptylist.append(inlist)
    return emptylist

def insertPixelList(pixels,image):
    height=len(image)
    width=len(image[0])
    for i in pixels:
        x=i['x']
        y=i['y']
        if locationValid(x,width,y,height):
            image[y][x]=i['pixel']
    return None

def writePPM(image,filename):
    height=len(image)
    width=len(image[0])
    with open(filename,'w') as f:
        f.write('P3\n')
        f.write(f'{width} {height}\n')
        f.write('255\n')
        for row in image:
            for pixel in row:
                f.write(f"{pixel['r']} {pixel['g']} {pixel['b']}\n")
    return None

def addCircleToList(x,y,r,color,pixels):
    for xT in range(x-r,x+r+1):
        for yT in range(y-r,y+r+1):
            dict1={}
            dx=xT-x
            dy=yT-y
            distance_square=dx**2+dy**2
            if distance_square<=r**2:
                dict1['x']=xT
                dict1['y']=yT
                dict1['pixel']=color
                pixels.append(dict1)
    return None

def addRectangleToList(x1,x2,y1,y2,pixel,pixels):
    for i in range(min(x1,x2),max(x1,x2)+1):
        for j in range(min(y1,y2),max(y1,y2)+1):
            dict2={}
            dict2['x']=i
            dict2['y']=j
            dict2['pixel']=pixel
            pixels.append(dict2)

def yourPictureFunction():
    image = generateEmptyPicture(400, 300)
    pixels = []

    sky_color=convertPixel([50, 130, 246])
    addRectangleToList(0, 399 ,0, 299, sky_color, pixels)

    sun_color = convertPixel([255, 255, 0])
    addCircleToList(80, 60, 30, sun_color, pixels)
    
    grass_color=convertPixel([55, 125, 34])
    addRectangleToList(0, 399, 200, 299, grass_color, pixels)

    house_color = convertPixel([139, 69, 19])
    addRectangleToList(250, 350, 150, 250, house_color, pixels)

    window_color = convertPixel([255, 255, 255])
    addCircleToList(330, 180, 10, window_color, pixels)
    
    roof_color = convertPixel([150, 30, 30])
    addRectangleToList(240, 360, 130, 150, roof_color, pixels)

    trunk_color = convertPixel([110, 60, 20])
    addRectangleToList(175, 185, 180, 250, trunk_color, pixels)

    leaves_color = convertPixel([20, 100, 40])
    addCircleToList(180, 140, 40, leaves_color, pixels)
    
    insertPixelList(pixels, image)
    writePPM(image, "simple_test.ppm")
    print("success")

yourPictureFunction()
    

   
