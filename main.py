def averagePixel(listOfColor):
    if not listOfColor:
        return [0, 0, 0]
    else:
        total=[0, 0, 0]
        count=0
        for inlist in listOfColor:
            for color in inlist:
                total[0]+=color[0]
                total[1]+=color[1]
                total[2]+=color[2]
                count+=1
        if count==0:
            return [0, 0, 0]
        total[0]=int(total[0]//count)
        total[1]=int(total[1]//count)
        total[2]=int(total[2]//count)
        return total

def swapCool(listOfColor):
    for inlist in listOfColor:
        for color in inlist:
            a=color[1]
            color[1]=color[2]
            color[2]=a
    return None

def shiftImage(listOfColor,add_depth):
    for inlist in listOfColor:
        for color in inlist:
            for i in range(len(color)):
                color[i]+=add_depth
                if color[i]>255:
                    color[i]=255
                if color[i]<0:
                    color[i]=0

def createDarker(pixels, percentage):
    result = []
    for row in pixels:
        new_row = []
        for color in row:
            new_color = []
            for channel in color:
                new_value = int(channel * percentage)
                new_color.append(new_value)
            new_row.append(new_color)
        result.append(new_row)
    return result

def createStripes(t, n, color1, color2):
    image = []
    size = t * n
    for i in range(n):
        if i % 2 == 0:
            current_color = color1
        else:
            current_color = color2
        for _ in range(t):
            row = []
            for _ in range(size):
                row.append(current_color[:])
            image.append(row)
    return image
