import math
print()
print(" "*20 + "!!!! WELCOME TO PAINT CALCULATOR !!!!")
print()

def paint_cal(height, width, coverage):
    var = (height*width)/coverage

    # if int(var) < var:
    #     return int(var) + 1
    # else:
    #     return int(var)    

    return math.ceil(var)

if __name__ == '__main__':
    wall_height = int(input("Height of the wall: "))
    wall_width = int(input("Width of the wall: "))
    coverage = int(input("Coverage area: "))
    print()
    print(f'You need to buy {paint_cal(wall_height, wall_width, coverage)}l of paint.')
    print()
