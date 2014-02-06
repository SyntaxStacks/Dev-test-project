from spaces import Spaces

class JustifiedText():
    def __init__(self, columnSize):
        self.columnSize = int(columnSize)
        self.justifiedLines = []
        self.tmpLine = []

    def __addLine(self):
        if(len(self.tmpLine) > self.columnSize):
            raise Exception("Provided line is too long: " + self.tmpLine)
        justifiedLine = ''.join(self.tmpLine)
        # print(justifiedLine)
        self.justifiedLines.append(justifiedLine)
        self.tmpLine = []
    
    def __justifyLine(self):
        self.tmpLineSpaces = Spaces(self.tmpLine)
        self.tmpLineSpaces.catalogSpaces()
        self.__padLine()
        self.__addLine()


    def __padLine(self):
        paddingCount = self.columnSize - len(self.tmpLine)
        # print("padding count: " + str(paddingCount))
        if paddingCount <= 0:
            return
        middlePlace = self.tmpLineSpaces.getMiddleSpacePlace()
        # print("middlePlace: " + str(middlePlace))
        for i in range(0, paddingCount):
            # print("looping through space count: " + str(i))
            if i % 2 != 0:
                walkForwardPlace = middlePlace + (i % middlePlace)
                # print("walk forward place: " + str(walkForwardPlace))
                location = self.tmpLineSpaces.getLocation(walkForwardPlace)
                # print("walk forward location: " + str(location))
                self.tmpLine.insert(location, ' ')
            else:
                walkBackPlace = middlePlace - (i % middlePlace)
                # print("walk backward place: " + str(walkBackPlace))
                location = self.tmpLineSpaces.getLocation(walkBackPlace)
                # print("walk back location: " + str(location))
                self.tmpLine.insert(location, ' ')

    def checkLineFull(self, word):
        # print("count of tmpLine: " + str(len(self.tmpLine)))
        nextLineSize = len(self.tmpLine) + len(word)
        metLineSize = nextLineSize >= self.columnSize
        if metLineSize:
            # print(self.tmpLine)
            self.__justifyLine()

    def addWord(self, word):
        # todo: handle case where word is longer than columnSize
        # print(word)
        self.checkLineFull(word)
        if len(self.tmpLine) >= 1:
            word = " " + word
        for char in word:
            self.tmpLine.append(char)
        if '\n' in word:
            self.__addLine()

    def finalizeJustify(self):
        self.__addLine()

    def printJustifiedText(self):
        # print("made it to printing justified text")
        for line in self.justifiedLines:
            print(line)
