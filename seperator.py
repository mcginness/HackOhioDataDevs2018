from operator import attrgetter

class songs():
    def __init__(self, title):
        self.title = title
        self.words = []
        self.listOfPairs = []
    

class wordCountPair():
        def __init__(self,word,count):
            self.word = word
            self.count = count
        

def fillPairs(song):
    

    def checkList(word,list):
        for pairs in list:
            if word == pairs.word:
                return True
                break
        return False

    def incrementWord(word,list):
        for pairs in list:
            if pairs.word == word:
                pairs.count += 1

    listOfPairsCosmogony= []
 
    for wordsInSong in song.words:
        if checkList(wordsInSong,listOfPairsCosmogony):
           incrementWord(wordsInSong,listOfPairsCosmogony)
        else:
            temp = wordCountPair(wordsInSong,1)
            listOfPairsCosmogony.append(temp)
   
    return  listOfPairsCosmogony              


def printPairs(song,name):
        
    
    pairList = fillPairs(song)
    sortedList = sorted(pairList, key= attrgetter('count'))
    sortedList.reverse()
    outFile = open(".\counts\\"+name+"WordMap.txt","w")

    for word in sortedList:
        outFile.write(word.word + " " +str(word.count) +" \n")
    outFile.close()


def pullWords(file):
        #creating file handlers
        slash = "\\"
        fileName = file+".txt"
        outputFile = '.\words'+slash+file+"Words.txt"
        
        readFile = open((fileName), "r")
        content = readFile.readlines()
        outFile = open((outputFile),"w")

        #screating new song
        song = songs("")

        
        #iterating through each line of the file
        #then parsing each line into seperate words
        for lines in content:
        
            wordsInLine = removeChars(lines)
            
            for word in wordsInLine.split():
                song.words.append(word)
            

        #printing songs to the file
        printSong(song,outFile)
    
        #close handles
        readFile.close
        outFile.close

        return song
        

def printSong(song,out):
        for word in song.words:
            out.write(word+"\n")

def removeChars(word):
        
        returnList = []
       
        #creating list of seperators 
        removingChars = "!@#$%^&*()_-+=;:\\\",<.>/?—[]"
        seperators = [] 
        for chars in removingChars:
            seperators.append(chars)
    
    #creating list of induviual characters
        charList = []
        for chars in word:
            charList.append(chars)

    #iterating through each seperator then characters and removing the seperators
        finalWord=""
        for seps in seperators:
           
            for i,chars in enumerate(charList):
                if (chars == seps):
                    charList[i] = " "
        
        for chars in charList:
            finalWord += chars
        
        return finalWord.lower()
        

"""
song = "reborn"


#song = "testText"
#outFile ="testTextWords"

songReturn = pullWords(song)
pairList = fillPairs(songReturn)

outFile = open("test.txt","w")


for word in pairList:
    outFile.write(word.word + " " +str(word.count) +" \n")
outFile.close()


strings = "A^b,   c@d"
print(strings)
x = removeChars(strings)
for words in x:
    print(words)"""