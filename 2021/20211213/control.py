# folder="example"
folder="puzzle"

def getEmptyPaper(size):
    ary    = []
    x_size = size[0]
    y_size =  size[1]

    for y in range(y_size+1):
        temp_ary=[]
        for x in range(x_size+1):
            temp_ary.append(" ")
            # temp_ary.append(str(x)+","+str(y))
        ary.append(temp_ary)
    return ary

def getSizePaper(): #return x, y (max value in file.)
    x = y = 0
    mark_file = open(folder+"/mark.txt", "r")
    lines     = mark_file.read().split("\n")
    for line in lines:
        mark = line.split(",")
        mark[0] = int(mark[0])
        mark[1] = int(mark[1])
        x = mark[0] if x < mark[0] else x
        y = mark[1] if y < mark[1] else y
    return x, y

def printPaper(paper):
    p = ""
    for y in paper:
        for x in y:
            # p+=str(x)
            p += "["+str(x)+"]"
        p += "\n"
    print(p)

def markPaper(paper, position, mark = "#"):
    x = position[0]
    y = position[1]
    # mark = mark if mark else "#"
    # print(x, y)
    paper[y][x] = mark
    return paper

def markPaperFromFile(paper):
    mark_file = open(folder+"/mark.txt", "r")
    mark_list = mark_file.read().split("\n")
    for item in mark_list:
        position = item.split(",")
        position[0] = int(position[0]) #x
        position[1] = int(position[1]) #y
        paper = markPaper(paper, position)
    return paper


def foldPaperY(paper, y):
    paper_split = []

    count = 0
    for y_item in paper:
        if(count < int(y)):
            paper_split.append(y_item)
        count+=1
    
    max_paper = len(paper)-1
    y_curr = 0
    for y_item in paper_split:
        x_curr = 0
        for x_item in y_item:
            x_target = x_curr
            y_target = max_paper-y_curr
            paper_split[y_curr][x_curr] = "#" if  x_item == "#" or paper[y_target][x_target] == "#" else x_item
            x_curr += 1
        y_curr += 1

    paper = paper_split

    return paper

def foldPaperX(paper, x, debug = 0):
    fullSize = getSizePaper()
    paper_split = getEmptyPaper([x-1, len(paper)-1])
    # Add Curr Paper Mark:
    y_curr=0
    for y_item in paper_split:
        x_curr = 0
        for x_item in y_item:
            paper_split[y_curr][x_curr] = paper[y_curr][x_curr]
            x_curr += 1
        y_curr += 1
    # Add Paper fold:
    y_curr = 0
    for y_item in paper_split:
        x_curr = 0
        for x_item in y_item:
            x_target = (len(paper[0])-1)-x_curr
            y_target = y_curr
            # print(y_target, x_target)
            # paper_split[y_curr][x_curr] = "x" if paper[y_target][x_target] else "b"
            paper_split[y_curr][x_curr] = "#" if x_item == "#" or paper[y_target][x_target] == "#" else x_item
            x_curr += 1
        y_curr += 1
    return paper_split

def foldPaperByFile(paper):
    fold_file = open(folder+"/fold.txt", "r")
    for item in fold_file.read().split("\n"):
        if("fold along x=" in item):
            value = int(item.replace("fold along x=", ""))
            paper = foldPaperX(paper, value)
        elif("fold along y=" in item):
            value = int(item.replace("fold along y=", ""))
            paper = foldPaperY(paper, value)
    return paper
