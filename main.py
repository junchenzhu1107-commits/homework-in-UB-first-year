def serialize(list1):
    output=[]
    for inlist in list1:
        for i in inlist:
            output.append(i)
    return output

def createFactorRows(r):
    if r==0:
        return []
    else:
        outlist=[]
        for how_many in range(r):
            inlist=[]
            for devisible in range(how_many+1):
                if (how_many+1) % (devisible+1)==0:
                    inlist.append(1)
                else:
                    inlist.append(0)
            outlist.append(inlist)
    return outlist

def truncateRows(list3):
    if not list3:
        return []
    final=[]
    length=len(list3[0])
    for i in range(len(list3)):
        if len(list3[i])<length:
            length=len(list3[i])
    for g in list3:
        empty=[]
        for f in range(length):
            empty.append(g[f])
        final.append(empty)
    return final

def collapseRows(list4):
    for i in range(len(list4)):
        inlist=list4[i]
        a=inlist[0]
        for num in inlist:
            if num>a:
                a=num
        list4[i]=[a]
    return None

def collapseCols(list5):
    if len(list5)==0:
        return None
    else:
        num_cols=len(list5[0])
        max_values=[]
        for i in range(num_cols):
            max_val=list5[0][i]
            for row in range(len(list5)):
                if list5[row][i]>max_val:
                    max_val=list5[row][i]
            max_values.append(max_val)
        list5.clear()
        list5.append(max_values)        
        return None







