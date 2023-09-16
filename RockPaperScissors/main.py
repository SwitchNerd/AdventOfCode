score = 0
rock1 = 'X'
paper1 = 'Y'
scissors1 = 'Z'

rock2 = 'A'
paper2 = 'B'
scissors2 = 'C'

with open("outcomes.txt",'r') as data:
    for comb in data.readlines():
        enemy = comb[0]
        user = comb[2]

        #getting the decisions score
        if user == rock1:
            score += 1
        elif user == paper1:
            score += 2
        elif user == scissors1:
            score += 3
            

        #getting the match result score
        #user wins
        if user == rock1 and enemy == scissors2:
            score = score + 6
        elif user == paper1 and enemy == rock2:
            score = score + 6
        elif user == scissors1 and enemy == paper2:
            score = score + 6
            
        #draw
        elif user == rock1 and enemy == rock2:
            score = score + 3
        elif user == paper1 and enemy == paper2:
            score = score + 3
        elif user == scissors1 and enemy == scissors2:
            score = score + 3
            
        #enemy wins
        elif user == rock1 and enemy == paper2:
            score = score + 0
        elif user == paper1 and enemy == scissors2:
            score = score + 0
        elif user == scissors1 and enemy == rock2:
            score = score + 0
    
    print(score)