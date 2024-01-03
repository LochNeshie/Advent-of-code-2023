#import and open stuff
import re

f = open('/Users/Neshome/Desktop/Random/Advent_of_code/Input4.txt', 'r')
input = f.read().split('\n')

dupl_dictionary = {}
for line in input:
    print('\nNew card')
#find and save the card number
    grabcard = line.split(':') #separate line into game number and data
    grabcard = grabcard[0].split(' ') #split game number into 'game' and 'number'
    while('' in grabcard): #remove empty entries
        grabcard.remove('')
    cardnr = grabcard[1] #save the number
    print('Cardnumber: ', cardnr)
#check if the cardnr is in the dictionary
    if cardnr not in dupl_dictionary: #if it isn't: add it with value 1
        print('New card')
        dupl_dictionary[cardnr] = 1
    else: #if it is: add 1 to the current value
        print('Current duplicates: ', dupl_dictionary[cardnr])
        dupl_dictionary[cardnr] += 1
#check the amount of duplicates at that cardnumber
    dupl = dupl_dictionary[cardnr]
    print('Duplicates counting this one: ', dupl)
#look at winning numbers        
    #remove the card number etc
    info = re.sub('Card \d+: ', '', line)
    #split into two pieces using the bar in the middle, lists with winning and my numbers
    info = info.split(' | ')
    winning = info[0]
    winning = winning.split(' ')
    while('' in winning): #remove empty entries
        winning.remove('')
    mine = info[1]
    mine = mine.split(' ')
    while('' in mine): #remove empty entries
        mine.remove('')
    cardnext = cardnr #prep the cardnumber for the next card, aka the one that will be duplicted
    #check my numbers for winning numbers
    for number in winning:
        if number in mine:
            print(number, ' is a match!')
        #add a duplicate to the dictionary at the next cardnumber,
        #take the duplicates of original card into account
            cardnext = str(int(cardnext)+1) #take the next cardnumber
            if cardnext in dupl_dictionary:
                dupl_dictionary[cardnext] += 1*dupl
                print('Card ', cardnext, ' already found, adding ', dupl, ' duplicates')
                print('Result: ', dupl_dictionary[cardnext])
            else:
                dupl_dictionary[cardnext] = 1
                print('Card', cardnext, ' is new, adding 1 duplicate')
                print('Result: ', dupl_dictionary[cardnext])
        else:
            print('No match')
#make a list of all the duplicate numbers, aka the dictionary values
dupl_list = list(dupl_dictionary.values())
print('All duplicates: ', dupl_list)
print('Amount of cards: ', len(dupl_list))

#make a sum of all the duplicates = answer
answer = sum(dupl_list)
print('Sum of duplicates: ', answer)

### het werkt, maar als de laatste kaart wel doorverwijst dan werkt het niet meer
#dat ook fixen:
#als de laatste dupl_dict key groter is dan het laatste kaartnr -> verwijderen entry