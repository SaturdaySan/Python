num = int(input('digita il numero di host per la subnet: '))

def binaryConvert(num):
    return bin(num)[2:]

print(binaryConvert(num))

def hostBits(num):
    posCounter = 0
    import math
    for number in binaryConvert(num):
        posCounter+=1
    
    print(math.pow(2,posCounter))

    
hostBits(num)