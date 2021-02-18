'''
EXERCISES taken from the book ' python basic by mercury learning and information '
'''
# Write a program to swap two numbers.
def swapper (a : int , b : int):
    (a,b) = (b,a)
    return a , b

# Ask the user to enter the coordinates of a point and find the distance of the point from the origin.
def originToPoint(x, y):
    import math
    calc = math.hypot(x,y)
    return calc

# Ask the user to enter two points (x and y coordinates) and find the ­distance between them.
def distanceTwoPoints(x : list , y : list):
    import math
    distance = math.dist(x,y)
    return distance

# Ask the user to enter three points and find whether they are collinear. 
def collinear(x : list , y : list , z : list):
    if x[0] == y[0] and y[0] == z[0]:
        print('they are collinear')
        return True
    else :
        print('they are not collinear')
        return False

# Ask the user to enter two points and find if they are at equal distances from the origin
def equalOriginDistance(pointX : list , pointY : list):
    import math
    distancePointX = math.hypot(pointX[0] , pointX[1])
    distancePointY = math.hypot(pointY[0] , pointY[1])
    if distancePointX == distancePointY:
        print("they're distance from the origin is equal")
        return True 
    else : 
        print('theire distance from the origin is not equal')
        return False

# Ask the user to enter 4 points and arrange them in order of their distances from the origin
