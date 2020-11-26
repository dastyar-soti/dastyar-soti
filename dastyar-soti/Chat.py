import Dictionary
#this is a chat class that stores verb , noun , arrangmen of sentence
#in nutshell , it's class that program will understand what to do.
class Chat:
    #this is array for see the arrangment of VERB , Noun etc ... 
    #ForExample : GIVE ME A BOOK
    #["GIVE" , "BOOK"]
    #it is regular words
    listOfArrangement=[]
    #this is A words
    listOfArrangementInA = []
    #split version of input by (SPACE)
    splitted = []
    #verb , obj , subj , etc
    verb = ""
    obj = ""

    #methods
    def __init__(self , inp)
        splitted = inp.split()
        detect()
    #method for detection of arrangment , verbs , nouns and ...
    #it will fill the listOFArrangmentInA and the other one
    def detect(self):
        #search every word in sentence
        for i in self.splitted :
            #if the word (i) is a verb or noun or IGNORE-TYPE
            if(isVerb(i)):
                listOfArrangementInA.append("verb")
                listOfArrangement.append(i)
            elif(isNoun(i)):
                listOfArrangementInA.append("noun")
                listOfArrangement.append(i)
            elif(isIgnoreType(i)):
                #nothing in particullar , we just ignore this word
                continue

            
    #used in detect , detect if the WORD is verb or is not
    def isVerb(self , word):
        #if the word is already in dictionary
        if (Dictionary.getA(word) == "verb"):
            return True
        #If the word have ING or ED at end
        if()
    #used in detect , detect if the WORD is verb or is not
    def isNoun(self , word):
        continue
    def isIgnoreType(self , word):
        continue
        


#parameter that shows when should it quit input
quitVal = False

while(quitVal != True):
    inp = input()
    cht = Chat(inp)

    #out can be WORK or ANSWER
    #NULL 4 work
    #ANSWER 4 answer
    #out = TODO
    #print (out)
