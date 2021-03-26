# this function just convert the number that it receives as input in a binary one
def binaryConvert(num : int):
    return bin(num)[2:]


#this function receive a number as input and it give as output the number of host 
def hostBits(hosts : int):
    '''
    #Version 1
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
    '''
    cvrt = binaryConvert(hosts)
    print(cvrt)
    import math
    bitsHost = 0
    while True :
        if int(math.pow(2,bitsHost)) > hosts :
            return bitsHost
            break
        else : 
            bitsHost += 1
    
# this functions  needs an int as input which represents the number of host
#  that you actually need as subnets then it return as output the number of bits dedicated for the subnets
def subnetBits(subnets : int):
    cvrt = binaryConvert(subnets)
    print(cvrt)
    import math
    bitsSubnet = 0
    while True :
        if int(math.pow(2,bitsSubnet)) >= subnets :
            return bitsSubnet
            break
        else : 
            bitsSubnet += 1


print(hostBits(4) , subnetBits(4))