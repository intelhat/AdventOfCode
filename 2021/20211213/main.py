from control import *

size = getSizePaper()
paper = getEmptyPaper(size)
paper = markPaperFromFile(paper)
paper = foldPaperByFile(paper)

printPaper(paper)
