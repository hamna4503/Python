#2.   A ladder put up right against a wall will fall over unless put up at a certain angle
# less than 90 degrees. Given variables length and angle storing the length of the ladder
# and the  angle that  it  forms  with  the  ground  as  it  leans  against  the  wall,
# write  a  Python  expression involving length and angle that computes the height reached by the
# ladder.
# Evaluate the expression for these values of length and angle:
#(a)16 feet and 75 degrees (b)20 feet and 0 degrees (c)24 feet and 45 degrees (d)24 feet and 80 degrees
#Note: You will need to use the trig formula:
#height = length * sin(angle)
#The math module sin() function takes its input in radians. You will thus need to convert the angle given in degrees to the angle given in radians using:
#radians = π * degrees / 180
import math
length=int(input("Enter the length of the ladder in ft: "))
degrees=int(input("Enter the angle in degrees: "))
angle=math.pi* degrees/180
height = length * math.sin(angle)
print("The height is",height,"ft.")
