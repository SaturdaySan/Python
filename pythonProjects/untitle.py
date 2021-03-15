num = int(input('digita il numero di host per la subnet: '))

# this function just convert the number that it receives as input in a binary one
def binaryConvert(num : int):
    return bin(num)[2:]


#this function receive a number as input and it give as output the number of host 
def hostBits(num : int):
    posCounter = 0
    import math
    for number in binaryConvert(num):
        posCounter+=1
    relHostN = math.pow(2,posCounter)
    if relHostN-2 < 2:
        posCounter+=1
        return posCounter
    else:
        return posCounter
        
    

def subnetBits(num : int):
    cvrt = binaryConvert(num)
    subBits = len(str((cvrt)))
    import math
    numPow = math.pow(2,len(str(cvrt)))
    if num <= numPow :
        subBits = subBits - 1
        return subBits 
    else:
        return subBits 
    
    return subBits
    
'''bit dedicati agli host" , hostBits(num) , "bit dedicati alle subnet" ,'''

