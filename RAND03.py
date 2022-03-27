#.3 Define two lists dice1 and dice2, holding
# numbers from 1 to 6 ,Design a python program  that start playing with two dices for two players
from random import *
dice1=[1,2,3,4,5,6]
dice2=[1,2,3,4,5,6]
print("Dice one gave: ",sample(dice1,1))
print("Dice two gave: ",sample(dice2,1))
