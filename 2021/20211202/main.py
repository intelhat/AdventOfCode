dir = "exm"
dir = "puzzle"

hrz   = 0 #horizan
depth = 0 #depth
aim   = 0

def getProduces():
    global hrz, depth, aim
    produces = 0
    data     = open(dir+"/data.txt", "r")
    data     = data.read().split("\n")
    
    for item in data:
        item_split = item.split(" ")
        direct     = item_split[0]
        size       = int(item_split[1])
        if(direct == "forward"):
            depth += (aim*size)
            hrz += size
            # print("f"+str(size)+": add "+str(size)+" to hrz is "+str(hrz)+" dept "+str(aim)+" * "+str(size)+"="+str(depth))
        elif(direct == "down"):
            aim += size
            # print("d"+str(size)+": aim is "+str(aim))
        elif(direct == "up"):
            aim -= size
            # print("u"+str(size)+": aim is "+str(aim))
    
    produces = hrz * depth
    # print(hrz, aim, depth)
    return produces

produces = getProduces()

print(produces)