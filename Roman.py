roman = input("Enter a Roman Number to convert:")

#dictionary to map roman numerals to arabic values
romanVals = {
    "M":1000,
    "C":100,
    "L":50,
    "X":10,
    "V":5,
    "I":1
}

for letter in roman:
    print(letter,"-->",romanVals[letter])
    