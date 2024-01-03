#import and open stuff
import re

f = open('/Users/Neshome/Desktop/Random/Advent_of_code/Input4.txt', 'r')
input = f.read().split('\n')

pointlist = []
for line in input:
    #remove the card number etc
    info = re.sub('Card \d+: ', '', line)
    #split into two pieces using the bar in the middle
    info = info.split(' | ')
    #make a list with the winning numbers
    winning = info[0]
    winning = winning.split(' ')
    while('' in winning): #remove empty entries
        winning.remove('')
    print(winning)
    #make a list with my numbers
    mine = info[1]
    mine = mine.split(' ')
    while('' in mine): #remove empty entries
        mine.remove('')
    print(mine)
    #register the amount of matches
    matches = 0
    for number in winning:
        if number in mine:
            matches = matches+1
    print(matches)
    #points is 2 ^ (amount of matches-1) (watch out for macthes = 0 -> ^-1)
    if matches == 0:
        print('No winning numbers')
    else:
        matches = matches-1
        points = 2**matches
        print(points)
        #add all these points to point list
        pointlist.append(points)
#take the sum = answer
answer = sum(pointlist)
print(answer)