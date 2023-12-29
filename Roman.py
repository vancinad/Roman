from enum import Enum
import random

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

def isArabic(i):
    '''
    return boolean indicating only arabic numerals in i
    '''
    #TODO: try converting to int (int(i)) and catch error instead of the less direct isdecimal()

    isArabic = False

    try:
        int(i)
        isArabic = True
    except:
        pass

    return(isArabic)

def isRoman(e):
    '''
    return boolean indicating only roman digits in e
    '''
    isRoman = False
    
    for letter in e:
        isRoman = letter in romanDigits #confirm this character is a Roman 'digit'
        if not isRoman:
            break #first non-Roman digit forces exit

    return isRoman

def toArabic(roman):
    '''
    Alternate (simplified) method of converting
    '''
    val = 0
    for i in range(0,len(roman)-1):
        iVal = romanDigits[roman[i]]

        #subtracting if nextVal is greater than iVal
        nextVal = romanDigits[roman[i+1]]
        sign = -1 if (nextVal > iVal) else 1

        val+=iVal*sign

    val+=romanDigits[roman[len(roman)-1]] #last is always added

    return val

    # end: toArabic()

def optimizeRoman(r):
    #TODO: implement this optimization
    '''
    given an r of 4 Roman digits (e.g. 'CCCC') convert it to an optimized equivalent, e.g. 'CD'
    '''
    lastChar = r[-1]
    firstChar = r[0]

    rVal = toArabic(r)
    
    return r #Just return input value for now...

    #end: optimizeRoman()

def toRoman_top_down(arabic):
    '''
        Starting from the high digits...

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
            if i > 0:
                #f = "{{:{c}<{l}}}".format(c=r,l=i)
                #add = f.format('')
                add = ''.ljust(i,r)
                if i > 3:
                    add = optimizeRoman(add)
                    #too many sequential numerals (e.g. "CCCC" s/b "CD")
                roman+=add
                remaining -= i * romanDigits[r]
                if remaining == 0: break
    return roman
    #end: toRoman_top_down()

def toRoman(arabic):
    roman = ""

    a = str(arabic)[::-1] #reverse input digits and convert to str
    exp = 0 #exponent
    for c in a:
        cVal = (int(c)*10**exp)
        exp += 1
        cRom = toRoman_top_down(cVal)
        roman = cRom + roman

    return roman
    #end toRoman()

def getInput():
    '''
    Return a dict with 'type':InputType, and 'value':entry
    '''

    inputResult = {'type':None}
    
    while type(inputResult['type']) is not InputType: #keep going until we get an ARABIC, ROMAN, or EXIT

        #get user input
        inputResult['value'] = input("Enter a Roman or Arabic number to convert (Enter to exit):").upper()

        if inputResult['value'] == "":
            inputResult['type'] = InputType.EXIT
        else:
            # is input numeric?
            if isArabic(inputResult['value']):
                inputResult['type'] = InputType.ARABIC
                inputResult['value'] = int(inputResult['value']) #return value as integer
            else:
                #check to see if it's a Roman number
                if isRoman(inputResult['value']):
                    inputResult['type'] = InputType.ROMAN
                else:
                    print("\'",inputResult['value'],"\' is no good. Use only valid Roman or Arabic numerals. Try again?") 
    
    return inputResult

# end: getInput()

def doTest(testCount = 5):
    '''
    run some tests with fixed inputs
    '''
    tList = list() #test input list
    rList = list() #result list

    #generate test values
    random.seed()
    for x in range(0,testCount):
        tList.append(random.randint(1,3999))
    tList.sort()

    print("Arabic to Roman tests:")
    for t in tList:
        r = toRoman(t)
        rList.append(r)
        print ("\tConverting {} ==> {}".format(t, toRoman(t)))

    #tList[0] = tList[0]+1 #force a mismatch to test the test

    #now convert the Romans back to Arabic and see if they match
    print("Roman to Arabic tests:")
    for x in range(0, len(rList)):
        a = toArabic(rList[x])
        m = f" !!! should be {tList[x]}" if a != tList[x] else " ok"
        print ("\tTest {}: {} ==> {}{}".format(x+1, rList[x], a, m))

def doUserInput():
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


'''
Mainline begins here
'''

doTest()
#doUserInput() #do all the things

