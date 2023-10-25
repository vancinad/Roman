#dictionary to map roman numerals to arabic values
romanVals = {
    "M":1000,
    "D":500,
    "C":100,
    "L":50,
    "X":10,
    "V":5,
    "I":1
}

def getInput():
    '''
    Return a string that is empty or contains valid Roman numerals
    '''
    inputOK = False
    
    while inputOK == False:
        n = input("Enter a Roman Number to convert (Enter to exit):").upper()

        if n == "":
            inputOK = True
            break

        try:
            for letter in n:
                v = romanVals[letter] #try retrieving a value with this key
                #print(letter,"-->",romanVals[letter])
            inputOK = True  #if the above loop completes, all numerals are valid
        except:
            print("\'",letter,"\' is no good. Use only valid roman numerals. Try again?") 
    
    return n
# end: getInput()

roman = getInput()
while roman != "":

    rLen = len(roman)  
    val = 0
    mode = "add"

    for i in range(rLen-1, 0, -1):
        rNumeral = roman[i]
        v1 = romanVals[rNumeral]
        
        if mode == "add":
            val += v1
        else:
            val -= v1

        # print("[",i,"] ", mode, " ", v1)
        prevVal = romanVals[roman[i-1]]
        if prevVal > v1:
            mode = "add"
        elif prevVal < v1:
            mode = "sub"

    i=0
    v1 = romanVals[roman[i]]
    # print("[",i,"] ", mode, " ", v1) 
    if mode == "add":
        val += v1
    else:
        val -= v1

    print (roman,"==>",val)

    roman = getInput()

