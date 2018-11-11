
def barcodeValidator(userInput) : #this function calculates that given input is a valid barcode number or not
        userInput = str(userInput) #casting int to string
        digitArray = list(userInput) #creating char array from string

        validator = 0
        value1 = 0
        value2 = 0

        for i in range(len(digitArray)):
            if i%2 == 0: #we have to sum even indexed numbers with even indexed, odd indexed with odd indexed.
                value1 = value1 + int(digitArray[i]) #to calculate summation, casting char to int.
            else:
                value2 = value2 + int(digitArray[i]) #to calculate summation, casting char to int.

        if len(digitArray) == 12:
            value2 = value2 - int(digitArray[11])  # calculations don't takes last digit of barcodes.
        if len(digitArray) == 13:
            value1 = value1 - int(digitArray[12])  # calculations don't takes last digit of barcodes.

        lastDigitOfValue1 = value1 % 10 #finding last digits.
        lastDigitOfValue2 = value2 % 10 #finding last digits.

        #Calculations below from here done according to PDF.

        x = lastDigitOfValue1*3
        y = x + lastDigitOfValue2

        lastDigitOfY = y % 10
        z = 10 - lastDigitOfY
        if len(userInput) == 12:
            if z == int(digitArray[11]):
                validator = 1
        if len(userInput) == 13:
            if z == int(digitArray[12]):
                validator = 1
        return validator

def barcodeStatus(userInput) : #This functions checks our given input for exceptions. If there is not exception,
    #calculates barcode's type.
    status = barcodeValidator(userInput)
    if status == 1 and len(str(userInput)) == 12 : #checks barcode is valid and 12 digit
        print("Barcode is a valid 12-digit barcode")
    if status == 1 and len(str(userInput)) == 13 : #checks barcode is valid and 13 digit
        print("Barcode is a valid 13-digit barcode")
    if (len(str(userInput)) != 13) and (len(str(userInput)) != 12) : #checks barcode lenght is valid
        raise Exception ("Barcode length is incorrect")
    if status == 0 and (len(str(userInput)) == 12 or len(str(userInput)) == 13) : #checks barcode lenght is valid but sum is not valid.
        raise Exception ("Invalid barcode.")
    try:
        val = int(userInput)
    except ValueError:
        print("That's not an int!")
