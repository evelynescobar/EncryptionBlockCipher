#Converts the Text to binary
def binText():
    text = input ( "Text that needs encoding: " )
    binaryText = "0"
    binaryText += '0'.join(format(ord(t), 'b') for t in text)

    return binaryText

#Converts Cipher Key to binary and if the Key is larger than 12 bits extracts the first 12 bits else it pads it to 12 bits
def binKey():
    cipherKey = input ( "Cipher Key: " )
    binaryKey = "0"
    binaryKey += '0'.join(format(ord(k), 'b') for k in cipherKey)

    if len(binaryKey) > 12:
        binaryKey = binaryKey[0:0+12]
    else:
        while len(binaryKey)%12 !=0 :
            text += "1"
            if len(binaryKey)%12 == 0:
                break
            else:
                text += "0"

    return binaryKey
        

#Pads the converted text if needed
def padText(text):
    paddingAdded = 0
    while len(text)%12 !=0 :
        text += "1"
        paddingAdded += 1
        if len(text)%12 == 0:
            break
        else:
            text += "0"
            paddingAdded += 1

    #If padding was added this converts how much padding to binary 
    if paddingAdded != 0:
        paddingAddedBinary = bin(paddingAdded).replace("0b", "")
        while len(paddingAddedBinary)%12 != 0:
            paddingAddedBinary = ( "0" + paddingAddedBinary )

    return text + paddingAddedBinary

#Reverses the string or 12 bit segment
def reverseString(text):
    return text[::-1]

#XORs using the Cipher Key or Previously XOR segment
def xorKey(segment, key):
    xorSegment = ""
    k = 0
    for s in segment:
        currentBit = int(s) ^ int(key[k])
        xorSegment += str(currentBit)
        k += 1

    return xorSegment

#Breaks string into 12 bit segments
def segmentTwelve(string):
    segments = [string[i:i+12] for i in range(0, len(string), 12)]

    return segments

#Does the actual Encryption Stuff, puts it all together
def cipherTwelve(segments, key):
    cipherStringFinal = ""
    prevXOR = ""

    index = 0
    for s in segments:
        if index == 0:
            segmentReversed = reverseString(s)
            xorSegment = xorKey(segmentReversed, key)
            cipherStringFinal += xorSegment
            prevXOR = xorSegment

            index += 1
        else:
            xorPrevSegment = xorKey(s, prevXOR)
            reverseXORSegment = reverseString(xorPrevSegment)
            encryptedSegment = xorKey(reverseXORSegment, key)
            cipherStringFinal += encryptedSegment
            prevXOR = encryptedSegment

    return cipherStringFinal 
    

#Key and text to Encrypt (Converts them to Binary)
binaryKey = binKey()
binaryText = binText()

#Pads the Binary text to 12 bits (if needed)
padded = padText(binaryText)

#Extracts the binary into 12 bit segments
twelveBitSegments = segmentTwelve(padded)

#Encrypts the text
encryptedString = cipherTwelve(twelveBitSegments, binaryKey)


print(encryptedString)
