score = 0
lose = 'X'
draw = 'Y'
win = 'Z'

rock2 = 'A'
paper2 = 'B'
scissors2 = 'C'

with open("outcomes.txt",'r') as data:
    for comb in data.readlines():
        enemy = comb[0]
        user = comb[2]

        if user == lose:
            score += 0
            if enemy == scissors2: #this means user is paper 
                score = score + 2
            elif enemy == rock2: #this means user is scissors
                score = score + 3
            elif enemy == paper2: #this means user is rock
                score = score + 1

        elif user == draw:
            score += 3
            if enemy == scissors2: #this means user is scissors 
                score = score + 3
            elif enemy == rock2: #this means user is rock
                score = score + 1
            elif enemy == paper2: #this means user is paper
                score = score + 2
        elif user == win:
            score += 6
            if enemy == scissors2: #this means user is rock 
                score = score + 1
            elif enemy == rock2: #this means user is paper
                score = score + 2
            elif enemy == paper2: #this means user is scissors
                score = score + 3
        
    print(score)