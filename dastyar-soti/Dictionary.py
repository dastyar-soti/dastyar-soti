dic = {
    "open" : {
        "a" : "verb",
        "meaning" : "open"
    },
    "take" : {
        "a" : "verb",
        "meaning" : "take"
    } , 
    "browser" : {
        "a" : "noun",
        "meaning" : "browser"
    } , 
    "chrome" : {
        "a" : "noun" ,
        "meaning" : "browser"
    },
    "to" : {
        "a" : "ignore"
    },
    "a" : {
        "a" : "ignore"
    }
}
def getA(word):
    word = word.lower()
    return dic[word]["a"]
