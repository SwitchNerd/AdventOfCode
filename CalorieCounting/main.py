test = []
_ = 0
max = 0
max1 = 0
max2 = 0
with open('datbase.txt', 'r') as data:
   test = data.readlines()
   
   for x in range(len(test)):
    if test[x] != '\n':
        _ += int(test[x])
    else:
       if max < _:
           max = _
       elif max1 < _:
           max1 = _
       elif max2 < _:
           max2 = _
       _ = 0
    #u are doing part 2, the problem with aboove code is that if the 2nd largest numbers gets registerd at max before the largest, then it is lost after the largest gets registered and so on
   print(max,max1,max2)