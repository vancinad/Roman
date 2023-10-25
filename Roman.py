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

inputMessage = "Enter a Roman Number to convert:"
roman = input(inputMessage).upper()
while roman != "":


    for letter in roman:
        print(letter,"-->",romanVals[letter])

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

        print("[",i,"] ", mode, " ", v1)
        prevVal = romanVals[roman[i-1]]
        if prevVal > v1:
            mode = "add"
        elif prevVal < v1:
            mode = "sub"

    i=0
    v1 = romanVals[roman[i]]
    print("[",i,"] ", mode, " ", v1) 
    if mode == "add":
        val += v1
    else:
        val -= v1

    print (roman,"==>",val)

    roman = input(inputMessage).upper()

