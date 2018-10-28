def removeChars(word):
        
        #temperary word holder
        temp = word
     
        #creating list of seperators 
        removingChars = "!@#$%^&*()_-+=;:\\\",<.>/?—[]".split()
       

     #iterating through each seperator and removing them
        for seps in removingChars:
            temp = temp.replace(seps, " ")
        
        return temp.lower()