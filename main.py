def countCharacters(filename,targetCharacters):
    dict1={}
    for target in targetCharacters:
        dict1[target]=0
    with open(filename,'r') as f:
        for line in f:
            line=line.strip()
            for c in line:
                if c in dict1:
                    dict1[c]+=1
    for target in targetCharacters:
        if dict1[target]==0:
            del dict1[target]
    return dict1

def secretMessage(filename,allLocation):
    list2=[]
    with open(filename,'r') as f:
        lines=f.readlines()
    for location in allLocation:
        line_index=location[0]
        word_index=location[1]
        
        line=lines[line_index].strip()
        words=line.split()
        list2.append(words[word_index])
    return list2

def generateGradeFile(filename, peoplesGrade):
    count = 0
    all_grades = ['A', 'B', 'C', 'D', 'F']
    with open(filename, 'w') as f:
        for grade in all_grades:
            f.write(grade + ':')
            
            if grade in peoplesGrade and len(peoplesGrade[grade]) > 0:
                names = peoplesGrade[grade]
                f.write(' ' + names[0])
                count += 1
                for i in range(1, len(names)):
                    f.write(' ' + names[i])
                    count += 1
            f.write('\n')
    return count
                
def replaceWords(filename1,filename2):
    with open(filename1) as f:
        with open(filename2,'w') as f2:
            for line in f:
                line=line.strip()
                words=line.split()
                if len(words)>0:
                    for i in range(len(words)):
                        if i==len(words)-1:
                            f2.write(str(len(words[i]))+'\n')
                        else:
                            f2.write(str(len(words[i]))+' ')
                else:
                    f2.write('0\n')
    return None

def translateFile(filename,dict1):
    content=''
    with open(filename) as f:
        lines=f.read()
    for char in lines:
        if char in dict1:
            content+=dict1[char]
        else:
            content+=char            
    with open(filename,'w') as f2:
        f2.write(content)
    return None

            




       

