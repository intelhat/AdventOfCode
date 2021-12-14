folder="exm"
# folder="puzzle"

def getInputData():
    sonar_file = open(folder+"/data_input.txt", "r")
    sonar_data =  sonar_file.read().split("\n")
    return sonar_data

def decreaseNoize(sonarData):
    result = ""
    char = ['A', '', '', '']
    char_time = [1, 4, 3, 2]
    char_curr = 'A'
    
    for item in sonarData:
        result += str(item)
        for char_item in char:
            result += " "+char_item
        result += "\n"
        for index in range(4):
            char_time[index] += 1
            if(char_time[index] > 3):
                if(char_time[index] > 4):
                    char_curr = chr(ord(char_curr) + 1)
                    char[index] = char_curr
                    char_time[index] = 1
                else:
                    char[index] = ""
    return result

def getInputData2():
    sonar_data = getInputData()
    sonar_data = decreaseNoize(sonar_data).split("\n")
    pointer = []
    for item in sonar_data:
        item_split = item.split(" ")
        item_split = arrayFilter(item_split)
        if(item_split):
            count = 0
            value = item_split[0]
            for name in item_split:
                if(count and name):
                    pointer = addPointer(pointer, name, value)
                count+=1
    return pointer
        
def addPointer(pointer, name, value):
    hasInPointer = 0
    key          = 0
    for item in pointer:
        if(item[0] == name):
            hasInPointer = 1
            index = key
        key += 1
    if(hasInPointer):
        pointer[index][1] = int(pointer[index][1]) + int(value)
    else:
        pointer.append([name, value])
    return pointer

def arrayFilter(array):
    res = []
    for item in array:
        if(item):
            res.append(item)
    return res

def loopSonar():
    data = getInputData()
    curr = 0
    result = 0
    for item in data:
        item = int(item)
        if(curr < item):
            result += 1
        # if(not curr):
        #     print(str(item)+" n/a no previous")
        # elif(curr < item) :
        #     result += 1
        #     print(str(item)+" increased "+str(result))
        # elif(curr > item):
        #     print(str(item)+" decreased")
        curr = item
    return result

def loopSonar2():
    data = getInputData2()
    curr = 0
    result = 0
    for item in data:
        name = item[0]
        value = int(item[1])
        if(curr < value):
            result += 1
        # if(not curr):
        #     print(name+":"+str(value)+" n/a no previous")
        # elif(curr < value):
        #     result += 1
        #     print(name+":"+str(value)+" increased "+str(result))
        # elif(curr > value):
        #     print(name+":"+str(value)+" descrease")
        curr = value
    return result

temp = loopSonar2()
print(temp)


# print(getInputData2())