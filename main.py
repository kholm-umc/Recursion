"""
Ken Holm

Purpose: The purpose of this program is to demonstrate recursion
"""

"""
This recursive function takes in a list.  It pop()s off the 
 last number in the list, then calls itself until there are
 no more items in the list.
"""
def recurseThroughList(listOfValues):
    value = listOfValues.pop()
    print(f"The value is {value}")
    if (len(listOfValues)) > 0:
        recurseThroughList(listOfValues)

"""
This function recursively computes the factorial of someNumber.
"""
def recursiveFactorial(someNumber):
    if someNumber == 1:
        return 1
    else:
        return(someNumber * recursiveFactorial(someNumber - 1))

"""
Recursive function used to solve the Tower of Hanoi game
See https://www.youtube.com/watch?v=8lhxIOAfDss&ab_channel=Computerphile
Play https://www.webgamesonline.com/towers-of-hanoi/index.php
"""
def solveTowerOfHanoi(numberOfDiscs, fromPosition, intermediatePosition, toPosition):
    if numberOfDiscs == 0:
        pass
    else:
        solveTowerOfHanoi(numberOfDiscs - 1, fromPosition, toPosition, intermediatePosition)
        print(f"Move disc from {fromPosition} to {toPosition}")
        solveTowerOfHanoi(numberOfDiscs - 1, intermediatePosition, fromPosition, toPosition)

myList = [1, "TWO", 3, "IV", int(25 / 5)]

print("Recursively walk through this list of values")
recurseThroughList(myList)

someInteger = int(input("Please provide a positive integer that won't break my computer: "))

print("Recursively compute the factorial of some number")
for someNumber in range(1, someInteger + 1):
    print(f"{someNumber}! {recursiveFactorial(someNumber)}")

input("Pause")

numberOfDisks = int(input("How many disks in the tower? "))
solveTowerOfHanoi(numberOfDisks, "Tower 1", "Tower 2", "Tower 3")
