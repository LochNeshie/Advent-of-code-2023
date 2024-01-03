#problem: doesn't fine overlapping things (eightwone). Solution is either write differently
#or install package that allows for overlapping things

import re

f = open('/Users/Neshome/Desktop/Random/Advent_of_code/Input1.txt', 'r')
input = f.read().split('\n')

#make a list to put all the coordinates in
coordinates = []

#if number -> save to numbers list
for line in input:
    #use findall to also find the words, put it all in a thing
    matches = re.finditer(r'(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))', line)
    numbersle = [match.group(1) for match in matches]
    #make a dictionary with word -> number
    numdict = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six': '6', 'seven': '7', 'eight':'8', 'nine':'9'}
    #change the words into numbers, put them in another thing
    numbers = []
    for char in numbersle:
        if char in numdict:
            numbers.append(numdict[char])
        else:
            numbers.append(char)
    print(numbers)
    #combine first and last numbers in other thing
    coorel = (numbers[0],numbers[-1])
    #make a thing to put coordinates in, put them in there
    coor = "".join(coorel)
    print(coor)
    #append coordinates with found coor, make them numbers
    coordinates.append(int(coor))
print(coordinates)

#see if we got the same amount of coordinates as lines (=1000)
length = len(coordinates)
print(length)

#sum
sum = sum(coordinates)
print("The answer is", sum)