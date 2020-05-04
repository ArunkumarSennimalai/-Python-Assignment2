import math
def calculateArea(r):
    return math.pi*r*r

if __name__ == "__main__":
    try:
        radius=float(input("Enter the radius:"))
        area = calculateArea(radius)
        print area
    except ValueError:
        print "Enter only numeric values"
    except Exception as e:
        print e
