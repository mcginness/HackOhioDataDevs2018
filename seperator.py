class songs():
    def __init__(self, title):
        self.title = title
        self.words = []

    def pullWords(fileName,outputFile):
        #creating file handlers
        fileName += ".txt"
        outputFile += ".txt"
        
        readFile = open((fileName), "r")
        content = readFile.readlines()
        outFile = open((outputFile),"w")

        #screating new song
        song = songs("")

        
        #iterating through each line of the file
        #then parsing each line into seperate words
        for lines in content:
        
            words = removeChars(lines)
            for word in words:
                song.words.append(word)
            

    
        printSong(song,outFile)
    
        #close handles
        readFile.close
        outFile.close
        

    def printSong(song,out):
        for word in song.words:
            out.write(word)

    def removeChars(word):
        
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
        for seps in seperators:
            for  i,chars in enumerate(charList):
                if (chars == seps):
                    charList[i] = " "
                
                    
        return charList
        
       
"""aa
song = "reborn"
outFile = "rebornWords"

#song = "testText"
#outFile ="testTextWords"

pullWords(song,outFile)

strings = "A^b,   c@d"
print(strings)
x = removeChars(strings)
for words in x:
    print(words)"""