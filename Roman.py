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
rDigitsKeysList = list(romanDigits.keys())
rDigitsValsList = list(romanDigits.values())

def isArabic(i):
    '''
    return boolean indicating input is an arabic integer
    '''

    try:
        int(i)
        isArabic = True
    except:
        isArabic = False

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
    Convert roman to arabic
    '''
    arabic = 0
    for i in range(0,len(roman)-1):
        iVal = romanDigits[roman[i]]

        #subtracting if nextVal is greater than iVal
        nextVal = romanDigits[roman[i+1]]
        sign = -1 if (nextVal > iVal) else 1

        arabic+=iVal*sign

    arabic+=romanDigits[roman[len(roman)-1]] #last is always added

    return arabic

    # end: toArabic()

def toRoman(arabic):
    '''
    Build a solution by:
    1) breaking the arabic number into its digit-value components
    2) for each component:
        a) look for a single-digit solution (e.g. 1000='M', 5='V')
        b) look for a two-digit solution (e.g. 900='CM', 40='XL')
        c) build a multi-digit solution (e.g. 8='VIII')
    3) append each component solution to the complete solution until done
    '''

    roman = "" #complete solution

    breakdown = segmentedNumber(arabic) #get a list of arabic digit component values
    for b in breakdown:
        thisDigit='' #solution for this component

        #find first roman value >= b -- the starting place for a one- or two- digit solution
        xv1 = -1 
        xr = range(len(rDigitsValsList)-1,-1,-1)
        for x in xr: #walk backward through vals list
            if rDigitsValsList[x] >= b: 
                xv1 = x
                break

        if xv1 != -1:  # found a starting place
            if rDigitsValsList[xv1] == b: #found single-digit solution, so...
                thisDigit = rDigitsKeysList[xv1]
            else:
                # Look for a 2-digit solution
                xv2 = -1  # position indicator for "subtract" digit
                for x in range(len(rDigitsValsList)-1,xv1,-1):
                    if rDigitsValsList[xv1] - rDigitsValsList[x] == b:
                        xv2 = x  # Found a solution
                        break
                #concatenate the two characters
                if xv2 != -1: 
                    thisDigit = (rDigitsKeysList[xv2] +  # the 'subtract' digit 
                        rDigitsKeysList[xv1])  # the 'add' digit
        
        if thisDigit == '':
            # No single- or two-digit solution found
            thisDigit = toRoman_multichar(b)

        roman+=thisDigit

    return roman

    #end: toRoman()

def segmentedNumber(given):
    '''
    return a list of numbers -- thousands, hundreds, tens, ones -- that add to n.
    Example: 1999 ==> (1000, 900, 90, 9)
    '''
    rem = given
    ret = list()
    numDigits = len(str(given))
    for e in range(numDigits-1, 0, -1):
        div = 10**e
        i = rem / div
        n = div * int(i)
        ret.append(n)
        rem -= n
    if rem > 0: ret.append(rem)
    return ret

def toRoman_multichar(arabic):
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

        Note that this function will produce invalid Roman numerals containing sequences
        of more than three repeating Roman digits, as in the example above. It should only be used after
        the possibility of two-digit "subtract" solutions (e.g. "CD" vs. "CCCC") has been eliminated.
    '''

    remaining = arabic
    roman = ""
    while remaining > 0:
        for r in romanDigits:
            n = remaining / romanDigits[r]
            i = int(n)
            if i > 0:
                add = ''.ljust(i,r)
                roman+=add
                remaining -= i * romanDigits[r]
                if remaining == 0: break
    return roman
    #end: toRoman_multichar()

def getUserInput():
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
                inputResult['value'] = int(inputResult['value']) #return value as integer
                if inputResult['value'] <= 3999:
                    inputResult['type'] = InputType.ARABIC
                else:
                    print("Number needs to be 3999 or less. Try again?")
            else:
                #check to see if it's a Roman number
                if isRoman(inputResult['value']):
                    inputResult['type'] = InputType.ROMAN
                else:
                    print("\'",inputResult['value'],"\' is no good. Use only valid Roman or Arabic numerals. Try again?") 
    
    return inputResult

# end: getInput()

def doTest(t = 5):
    '''
    check the type of test data provided and run the appropriate test
    '''
    if isinstance(t,int):
        doTest_int(t)
    elif isinstance(t,list):
        doTest_list(t)
    else:
        print("'doTest() doesn't know what to do with type '{}'".format(type(t)))

def doTest_int(testCount = 5):
    '''
    Generate a list of random numbers and test
    '''
    #generate test values
    tList = list()
    random.seed()
    for x in range(0,testCount):
        tList.append(random.randint(1,3999))
    tList.sort()
    doTest_list(tList)

def doTest_list(tList):
    '''
    run tests with given list of arabic numbers
    '''
    rList = list() #result list

    print(f"Tests using {tList}:")
    for t in tList:
        r = toRoman(t)
        t2 = toArabic(r)
        m = "" if t2 == t else "!?!"
        print ("{}\tConverting {} ==> {} ===> {}".format(m, t, r, t2))

def doUserInput():
    inputResult = getUserInput()

    while inputResult['type'] is not InputType.EXIT:

        match inputResult['type']:
            case InputType.ROMAN:
                val = toArabic(inputResult['value'])
                print (inputResult['value'],"==>",val)
            case InputType.ARABIC:
                val = toRoman(inputResult['value'])
                print (inputResult['value'],"==>",val)
            
        inputResult = getUserInput()


'''
Mainline begins here
'''

doTest(20)  # auto-generate tests
doUserInput()  # let the user try

#doTest([9, 49, 529, 710, 758, 831, 1267, 1438, 1449, 1537, 1538, 2168, 2376, 2772, 3005, 3115, 3160, 3218, 3554, 3722])
