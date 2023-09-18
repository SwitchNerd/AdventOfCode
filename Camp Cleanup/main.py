
with open('assignments.txt', 'r') as assignements:
    for i in assignements.readlines():
        first_half  = i[:len(i)//2]
        second_half = i[len(i)//2:]
        print(first_half, second_half)
        