#import and open stuff
import re

f = open('/Users/Neshome/Desktop/Random/Advent_of_code/Input2.txt', 'r')
input = f.read().split('\n')

#make function1 for the collection of maximum instances of color
newcolors = {}
def finding_maxcolors(color,element):
    all = []
    for dict in element:
        if color in dict:
            all.append(dict[color])
        if len(all) > 0:
            new = max(all)
            newcolors[color] = new

#make function2 checking those maximum instances against what the bag was loaded with
possible_games = []
def checking_colors(gamenr,dict,color1, color2, color3,amount1,amount2,amount3):
    if dict[color1] <= amount1 and dict[color2] <= amount2 and dict[color3] <= amount3:
        possible_games.append(int(gamenr))

powers = []
for line in input:
    #find and save the game number, so that we can collect it if it was
    #possible according to function2
    grabgame = line.split(':') #separate line into game number and data
    grabgame = grabgame[0].split(' ') #split game number into 'game' and 'number'
    gamenr = grabgame[1] #save the number
    
    #split the input into usable parts: list of dictionaries per game for function1
    listdict = []
    info = re.sub('Game \d+: ', '', line) #remove the game number etc.
    info = info.split('; ') #split into subgames
    for sub in info: #turn each subgame into a dictionary, put in list
        subdict = {}
        sub = sub.split(', ')
        for tiny in sub:
            tiny = tiny.split(' ')
            subdict[tiny[1]] = int(tiny[0])
        listdict.append(subdict)
    finding_maxcolors('red',listdict)
    finding_maxcolors('blue',listdict)
    finding_maxcolors('green',listdict)
    power = newcolors['red']*newcolors['green']*newcolors['blue']
    powers.append(power)

ans = sum(powers)
print(ans)