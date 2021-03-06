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
    #list of Similarity Rate : for patterns and list of arrangment
    similarityRatePatternRate = []
    #TODO weigh for machine learning
    weighRatePattern = [[1] , [1] , [1]]
    #patterns of sentence like I WANT TO OPEN CHROME
    patterns = [ ["pronoun" , "verb" , "noun"] , ["verb" , "noun"] , ["pronoun" , "verb" , "verb" , "noun"]]

    #methods
    def __init__(self , inp)
        splitted = inp.split()
        detect()
    #method for detection of arrangment , verbs , nouns and ...
    #it will fill the listOFArrangmentInA and the other one
    def detect(self):
        #search every word in sentence
        for i in self.splitted :
            i = i.lower()
            #if the word (i) is a verb or noun or IGNORE-TYPE
            if(isVerb(i)):
                listOfArrangementInA.append("verb")
                listOfArrangement.append(i)
            elif(isNoun(i)):
                listOfArrangementInA.append("noun")
                listOfArrangement.append(i)
            elif(isPronoun(i)):
                listOfArrangementInA.append("pronoun")
                listOfArrangement.append(i)

            
    #used in detect , detect if the WORD is verb or is not
    def isVerb(self , word):
        #if the word is already in dictionary
        if (Dictionary.getA(word) == "verb"):
            return True
        #If the word have ING or ED at end
        if(word.endswith("ed") or word.endswith("ing")):
            #if the word is not in dictionary , go and add it #LEARNING TODO
            return True
        #ANOTHER WAY ? TODO
        return False
    #used in detect , detect if the WORD is verb or is not
    def isNoun(self , word):
        if (Dictionary.getA(word) == "noun"):
            return True
        return False
    def isPronoun(self , word):
        if (Dictionary.getA(word) == "pronoun"):
            return True
        return False
    def similarityRatePattern(self):
        for i in patterns: #i represent each pattern like ["pronoun" , "verb"]
            rate = 0 #rate for each pattern
            for j in len(i): #j represent each A like "pronoun" 
                if(i[j] == listOfArrangementInA[j]):
                    rate += 10
            #add rate variable to end of similarity array for calculation at end
            #weigh is added for more accurate results
            similarityRatePattern.append(rate * weigh)
        


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
