from removeChars import*
class pair():
    def __init__(self,key,value):
        self.key = key
        self.value = value
    def increment (self):
        self.value += 1

class incrementalPairMap():
        def __init__(self, dataList = []):
            self.queue = []
            self.fillPairs(dataList)
        
        def createFromFile(self, filePath):
 
            fileHandle = open((filePath), "r")
            content = fileHandle.readlines()
                    
            for lines in content:
                seperatedLine = removeChars(lines).split()
                self.fillPairs(seperatedLine)
            

            
            

        def fillPairs(self,data):   
         for key in data:
              self.add(key)
  
        def add(self,keyAdd):  
            if self.contains(keyAdd):
                self.increment(keyAdd)
            else:
                self.queue.append(pair(keyAdd,1))
                    

        def contains(self,keySearch):
            for pair in self.queue:
                if pair.key == keySearch:
                    return True
            return False

        def increment(self,keySearch):
          for pair in self.queue:
              if (pair.key == keySearch):
                  pair.increment()

        
        
        
        
        
        
        
        def sort(self,index):
            self.queue = sorted(self.queue, key = index)
            self.queue.reverse()    

        
        def findValue(self,keySearch):
            for keys in self.queue:
                if (keys.key == keySearch):
                    return keys.value
        
        def findkeys(valueSearch):
            listOfKeys = []
            for values in self.queue:
                if (values.value == valueSearch):
                    listOfKeys.append(keys.value)
            return listOfKeys
        def prettyPrint(self,filePath):
            fileWriter = open((filePath), "w")
            for pair in self.queue:
                fileWriter.write(pair.key + " " + str(pair.value) +"\n")