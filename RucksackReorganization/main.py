'''To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?'''

letter = ''

with open('rucksack.txt','r') as rucksack:
    for i in rucksack.readlines():
        first_half  = i[:len(i)//2]
        second_half = i[len(i)//2:]
        first_list = list(first_half)
        second_list = list(second_half)
        
        for x in first_list:
            for i in second_list:
                if x == i:
                    letter = x
                    print(x, i)
        print(letter)