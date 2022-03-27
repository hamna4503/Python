import math
radius=10
for i in range(4):
    dart_x=int(input("Enter dart x - coordinate:"))
    dart_y = int(input("Enter dart y - coordinate:"))
    dart_coordinate=(dart_x,dart_y)
    print(dart_coordinate)
    co_check=math.sqrt(math.pow(dart_x,2) + math.pow(dart_y,2))
    print( co_check<=radius)
