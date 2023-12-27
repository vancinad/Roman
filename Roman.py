from enum import Enum

InputType = Enum('Input Type', ['ROMAN','ARABIC','EXIT'])

#dictionary to map roman numerals to arabic values
romanDigits = {
    "M":1000,
    "D":500,
    "C":100,
    "L":50,
    "X":10,
    "V":5,
    "I":1
}

def onlyArabic(i):
    '''
    return boolean indicating only arabic numerals in i
    '''
    return(i.isdecimal())

def onlyRoman(e):
    for letter in e:
        inputOK = letter in romanDigits #confirm this character is a Roman 'digit'
        if not inputOK:
            break
    return inputOK

def toArabic(roman):
    '''
    Return Arabic value for roman string
    '''            
    rLen = len(roman)  
    val = 0
    mode = "add"

    for i in range(rLen-1, 0, -1):
        rNumeral = roman[i]
        v1 = romanDigits[rNumeral]
        
        if mode == "add":
            val += v1
        else:
            val -= v1

        # print("[",i,"] ", mode, " ", v1)
        prevVal = romanDigits[roman[i-1]]
        if prevVal > v1:
            mode = "add"
        elif prevVal < v1:
            mode = "sub"

    i=0
    v1 = romanDigits[roman[i]]
    # print("[",i,"] ", mode, " ", v1) 
    if mode == "add":
        val += v1
    else:
        val -= v1

    return val

def toRoman(arabic):
    '''
        Given 1964...
        divide by 1000 ==> 1.964
        int ==> 1, add 1 'M' ==> "M"
        subtract 'M' from initial ==> 964 as 'remaining'
        divide by 'D'(500) ==> 1.nnn
        int ==> 1, add 1 'D' ==> "MD"
        subtract 'D' from remaining == 464
        divide by 'C'(100) ==> 4.64
        int ==> 4, add 4 'C' ==> "MDCCCC"
        subtract 4x'C' from remaining ==> 64
        divide by 'L'(50) ==> 1.nnn
        int==>1, add 1 'L' ==> "MDCCCCL"
        subtract 'L' ==> 14
    '''
    remaining = arabic
    roman = ""
    while remaining > 0:
        for r in romanDigits:
            n = remaining / romanDigits[r]
            i = int(n)
            f = "{{:{c}<{l}}}".format(c=r,l=i)
            add = f.format('')
            if len(add) > 3:
                #too many sequential numerals (e.g. "CCCC" s/b "CD")
                pass #TODO: implement this optimization
            roman+=add
            remaining -= i * romanDigits[r]
    return roman

def getInput():
    '''
    Return a dict with 'type':InputType, and 'value':entry
    '''

    inputResult = {} # the dict to return

    inputOK = False
    
    while inputOK == False:
        entry = input("Enter a Roman or Arabic number to convert (Enter to exit):").upper()

        if entry == "":
            inputOK = True
            inputResult['type'] = InputType.EXIT
        else:
            # is input numeric?
            numeric = onlyArabic(entry)
            if numeric:
                inputOK = True
                inputResult['type'] = InputType.ARABIC
                inputResult['value'] = int(entry)
            else:
                #check to see if it's a Roman number
                roman = onlyRoman(entry)
                if roman:
                    inputOK = True
                    inputResult['type'] = InputType.ROMAN
                    inputResult['value'] = entry
                else:
                    print("\'",entry,"\' is no good. Use only valid roman numerals. Try again?") 
    
    return inputResult

# end: getInput()

'''
Mainline begins here
'''
inputResult = getInput()

while inputResult['type'] is not InputType.EXIT:

    match inputResult['type']:
        case InputType.ROMAN:
            val = toArabic(inputResult['value'])
            print (inputResult['value'],"==>",val)
        case InputType.ARABIC:
            val = toRoman(inputResult['value'])
            print (inputResult['value'],"==>",val)
        
    inputResult = getInput()

