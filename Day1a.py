f = open('/Users/Neshome/Desktop/Random/Advent_of_code/Input1.txt', 'r')
input = f.read().split('\n')

#seperate one row into seperate parts? -> not needed
#make a list to put all the coordinates in

coordinates = []

#if number -> save to numbers list
for line in input:
    numbers = []
    for char in line:
        if char.isdigit():
            numbers.append((char))
    print(numbers)
    #combine first and last numbers in other thing
    coorel = (numbers[0],numbers[-1])
        #make a thing to put coordinates in, put them in there
    coor = "".join(coorel)
    print(coor)
    #append coordinates with found coor, make them numbers
    coordinates.append(int(coor))
print(coordinates)

#sum
sum = sum(coordinates)
print(sum)